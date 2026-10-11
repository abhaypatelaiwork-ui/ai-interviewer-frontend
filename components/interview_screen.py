import streamlit as st
import time
import io
import numpy as np
from PIL import Image
from streamlit_mic_recorder import mic_recorder
from api_client import InterviewAPI
from tts_service import text_to_speech, cleanup_audio
from face_processor import frame_to_base64
from styles import (
    render_recording_waveform,
    render_speaking_waveform,
    render_thinking_waveform,
    render_idle_waveform,
    render_recording_header,
    render_success_header,
)


def render(api: InterviewAPI):
    # ===== HEADER =====
    idx = st.session_state.current_index + 1
    total = st.session_state.total_questions
    progress = idx / max(total, 1)
    
    h1, h2 = st.columns([4, 1])
    with h1:
        st.markdown(f"### Question {idx} of {total}")
    with h2:
        st.markdown(
            f'<div style="text-align:right;color:#64748b;font-weight:600;">{int(progress*100)}%</div>',
            unsafe_allow_html=True,
        )
    st.progress(min(progress, 1.0))
    
    st.markdown("")
    
    # ===== AUTO-SPEAK QUESTION =====
    if st.session_state.last_question_index != st.session_state.current_index:
        st.session_state.last_question_index = st.session_state.current_index
        st.session_state.spoken_answer = ""
        st.session_state.recording_stage = "idle"
        st.session_state.recording_started_at = None
        
        if st.session_state.get("current_audio"):
            cleanup_audio(st.session_state.current_audio)
            st.session_state.current_audio = None
        
        with st.spinner("🔊 Preparing the question..."):
            try:
                path = text_to_speech(st.session_state.current_question)
                st.session_state.current_audio = path
            except Exception as e:
                st.warning(f"TTS error: {e}")
    
    # ===== 2-COLUMN LAYOUT =====
    left, right = st.columns([1.1, 1], gap="large")
    
    # ============ LEFT: CAMERA + CV ANALYSIS ============
    with left:
        st.markdown("### 📹 Live Analysis")
        st.caption("Face detection + emotion + attention (CV-based)")
        
        camera_image = st.camera_input(
            "Camera",
            label_visibility="collapsed",
            key=f"cam_{st.session_state.current_index}",
        )
        
        last = None
        if camera_image:
            img = Image.open(io.BytesIO(camera_image.getvalue()))
            frame = np.array(img)
            try:
                b64 = frame_to_base64(frame)
                analysis = api.analyze_frame(st.session_state.session_id, b64)
                st.session_state.face_frames.append(analysis)
                last = analysis
            except Exception as e:
                st.error(f"Analysis error: {e}")
        else:
            if st.session_state.face_frames:
                last = st.session_state.face_frames[-1]
        
        if last:
            if not last.get("face_detected"):
                st.markdown(
                    '<div class="cv-panel danger">'
                    '<div style="font-weight:700;color:#991b1b;">❌ Face Not Detected</div>'
                    '<div style="color:#7f1d1d;font-size:0.9rem;margin-top:4px;">'
                    'Please face the camera with good lighting'
                    '</div></div>',
                    unsafe_allow_html=True,
                )
            elif last.get("face_count", 0) > 1:
                st.markdown(
                    f'<div class="cv-panel warn">'
                    f'<div style="font-weight:700;color:#854d0e;">⚠️ {last["face_count"]} Faces Detected</div>'
                    f'<div style="color:#713f12;font-size:0.9rem;margin-top:4px;">'
                    f'Only you should be in the frame'
                    f'</div></div>',
                    unsafe_allow_html=True,
                )
            else:
                emotion = last.get("emotion", "?")
                attention = last.get("attention_score", 0)
                st.markdown(
                    f'<div class="cv-panel">'
                    f'<div style="font-weight:700;color:#166534;font-size:1rem;margin-bottom:12px;">'
                    f'✅ Face Detected & Analyzed'
                    f'</div>'
                    f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">'
                    f'<div><div class="metric-label">Emotion</div>'
                    f'<div class="metric-value" style="font-size:1.3rem;">😊 {emotion.title()}</div></div>'
                    f'<div><div class="metric-label">Attention</div>'
                    f'<div class="metric-value" style="font-size:1.3rem;">{attention:.1f}/10</div></div>'
                    f'</div></div>',
                    unsafe_allow_html=True,
                )
        
        frames = st.session_state.face_frames
        if frames:
            detected = [f for f in frames if f.get("face_detected")]
            pct = (len(detected) / len(frames)) * 100
            st.markdown(
                f'<div style="margin-top:12px;color:#64748b;font-size:0.88rem;">'
                f'<b>Session:</b> {len(frames)} frames • {pct:.0f}% face present'
                f'</div>',
                unsafe_allow_html=True,
            )
    
    # ============ RIGHT: QUESTION + ANSWER ============
    with right:
        st.markdown("### 🎤 Question")
        st.markdown(
            f'<div class="question-box">{st.session_state.current_question}</div>',
            unsafe_allow_html=True,
        )
        
        # Question speaking
        if st.session_state.get("current_audio") and not st.session_state.spoken_answer:
            st.markdown(
                '<div style="text-align:center;color:#6366f1;font-weight:600;font-size:0.9rem;margin-bottom:4px;">'
                '🔊 Playing the question...'
                '</div>',
                unsafe_allow_html=True,
            )
            render_speaking_waveform()
            st.audio(
                st.session_state.current_audio,
                format="audio/mp3",
                autoplay=True,
            )
        
        st.markdown("")
        st.markdown("### ✍️ Your Answer")
        
        stage = st.session_state.recording_stage
        
        # ============ STATE 1: ANSWER CAPTURED → AUTO-SUBMIT ============
        if st.session_state.spoken_answer:
            render_success_header("Answer captured — submitting...")
            st.markdown(
                f'<div class="pro-card" style="padding:16px;margin-top:12px;">'
                f'<div class="metric-label">Transcribed</div>'
                f'<div style="color:#1e293b;margin-top:8px;font-size:0.95rem;line-height:1.6;">'
                f'{st.session_state.spoken_answer}'
                f'</div></div>',
                unsafe_allow_html=True,
            )
            time.sleep(1.5)
            _submit(api, st.session_state.spoken_answer)
        
        # ============ STATE 2: PROCESSING TRANSCRIPTION ============
        elif stage == "processing":
            st.markdown(
                '<div style="text-align:center;color:#6366f1;font-weight:600;font-size:0.9rem;margin-bottom:4px;">'
                '🧠 Processing your voice...'
                '</div>',
                unsafe_allow_html=True,
            )
            render_thinking_waveform()
        
        # ============ STATE 3: RECORDING ============
        elif stage == "recording":
            # Elapsed time check
            if st.session_state.recording_started_at is None:
                st.session_state.recording_started_at = time.time()
            
            elapsed = time.time() - st.session_state.recording_started_at
            
            render_recording_header(f"🔴 Listening — {int(elapsed)}s")
            render_recording_waveform()
            
            st.markdown(
                '<div style="text-align:center;color:#64748b;font-size:0.88rem;margin-top:4px;">'
                'Start speaking — recording will stop automatically after 3 seconds of silence'
                '</div>',
                unsafe_allow_html=True,
            )
            
            # Recording UI with start and stop controls
            audio = mic_recorder(
                start_prompt="▶️ Continue",
                stop_prompt="⏹️ Stop",
                just_once=True,
                key=f"mic_rec_{st.session_state.current_index}",
                format="webm",
            )
            
            if audio and audio.get("bytes"):
                st.session_state.recording_stage = "processing"
                try:
                    text = api.transcribe_audio(audio["bytes"], "audio.webm")
                    st.session_state.spoken_answer = text
                    st.session_state.recording_stage = "idle"
                    st.session_state.recording_started_at = None
                    st.rerun()
                except Exception as e:
                    st.error(f"Transcription fail: {e}")
                    st.session_state.recording_stage = "idle"
                    st.session_state.recording_started_at = None
        
        # ============ STATE 4: IDLE — SINGLE TAP TO START ============
        else:
            # Idle waveform
            render_idle_waveform()
            
            st.markdown(
                '<div style="text-align:center;color:#64748b;font-size:0.92rem;margin:8px 0 16px 0;">'
                'Press the button below, then start speaking. '
                'Recording will stop automatically after 3 seconds of silence.'
                '</div>',
                unsafe_allow_html=True,
            )
            
            # Single big button
            audio = mic_recorder(
                start_prompt="🎙️ Start Answering",
                stop_prompt="⏹️ Recording...",
                just_once=True,
                key=f"mic_start_{st.session_state.current_index}",
                format="webm",
                use_container_width=True,
            )
            
            if audio and audio.get("bytes"):
                st.session_state.recording_stage = "processing"
                try:
                    text = api.transcribe_audio(audio["bytes"], "audio.webm")
                    st.session_state.spoken_answer = text
                    st.session_state.recording_stage = "idle"
                    st.rerun()
                except Exception as e:
                    st.error(f"Transcription fail: {e}")
                    st.session_state.recording_stage = "idle"


def _submit(api, answer):
    try:
        r = api.submit_answer(st.session_state.session_id, answer)
        st.session_state.answers.append({
            "question": st.session_state.current_question,
            "answer": answer,
            "evaluation": r["evaluation"],
        })
        
        if st.session_state.get("current_audio"):
            cleanup_audio(st.session_state.current_audio)
            st.session_state.current_audio = None
        
        if r["is_complete"]:
            st.session_state.feedback = r["feedback"]
            st.session_state.is_complete = True
            st.session_state.screen = "feedback"
        else:
            st.session_state.current_question = r["next_question"]
            st.session_state.current_index += 1
            st.session_state.spoken_answer = ""
            st.session_state.recording_stage = "idle"
            st.session_state.recording_started_at = None
        
        st.rerun()
    except Exception as e:
        st.error(f"Submit fail: {e}")