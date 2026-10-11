import streamlit as st
import re
from styles import render_score_card, render_badge, render_stars


def parse_feedback(text: str) -> dict:
    r = {
        "score": None,
        "strengths": [],
        "weaknesses": [],
        "recommendation": None,
    }
    if not text:
        return r
    
    m = re.search(r'(\d+(?:\.\d+)?)\s*/\s*10', text)
    if m:
        r["score"] = float(m.group(1))
    
    for rec in ["Strong Yes", "Yes", "Maybe", "No"]:
        if rec.lower() in text.lower():
            r["recommendation"] = rec
            break
    
    section = None
    for line in text.split("\n"):
        low = line.lower()
        if "strength" in low:
            section = "s"
            continue
        if "weak" in low or "improve" in low:
            section = "w"
            continue
        if section and line.strip().startswith(("-", "•", "*", "1", "2", "3")):
            clean = line.strip().lstrip("-•*0123456789. )").strip()
            if clean:
                (r["strengths"] if section == "s" else r["weaknesses"]).append(clean)
    
    return r


def render(api):
    st.markdown("## ✅ Interview Complete")
    st.markdown(
        '<p style="color:#64748b;margin-top:-8px;">Your performance report is below</p>',
        unsafe_allow_html=True,
    )
    
    st.markdown("")
    
    data = parse_feedback(st.session_state.feedback)
    
    # Top row: Score + Stars + Recommendation
    c1, c2, c3 = st.columns(3)
    
    with c1:
        if data["score"]:
            render_score_card("Overall Score", f"{data['score']}/10", "🎯")
    
    with c2:
        if data["score"]:
            st.markdown(
                '<div class="score-card">'
                '<div style="font-size:1.4rem;">⭐</div>'
                '<div class="score-label">Rating</div>',
                unsafe_allow_html=True,
            )
            render_stars(data["score"])
            st.markdown('</div>', unsafe_allow_html=True)
    
    with c3:
        if data["recommendation"]:
            st.markdown(
                '<div class="score-card">'
                '<div style="font-size:1.4rem;">💼</div>'
                '<div class="score-label">Recommendation</div>',
                unsafe_allow_html=True,
            )
            render_badge(data["recommendation"])
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown("---")
    
    # Face analysis summary
    if st.session_state.face_frames:
        st.markdown("### 📹 Face Analysis Summary")
        
        frames = st.session_state.face_frames
        detected = [f for f in frames if f.get("face_detected")]
        
        if detected:
            avg_att = sum(f.get("attention_score", 0) for f in detected) / len(detected)
            emotions = [f.get("emotion") for f in detected if f.get("emotion")]
            dominant = max(set(emotions), key=emotions.count) if emotions else "unknown"
            pct = (len(detected) / len(frames)) * 100
            warnings = sum(1 for f in frames if f.get("warning"))
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                render_score_card("Face Presence", f"{pct:.0f}%", "👤")
            with c2:
                render_score_card("Avg Attention", f"{avg_att:.1f}/10", "🎯")
            with c3:
                render_score_card("Dominant Emotion", dominant.title(), "😊")
            with c4:
                render_score_card("Warnings", str(warnings), "⚠️")
        
        st.markdown("---")
    
    # Strengths + Weaknesses
    c_s, c_w = st.columns(2)
    
    with c_s:
        st.markdown("### ✅ Strengths")
        if data["strengths"]:
            for s in data["strengths"]:
                st.markdown(
                    f'<div class="pro-card" style="padding:14px 18px;margin:8px 0;'
                    f'border-left:4px solid #10b981;">✅ {s}</div>',
                    unsafe_allow_html=True,
                )
        else:
            st.info("See the full feedback for strengths")
    
    with c_w:
        st.markdown("### ⚠️ Areas to Improve")
        if data["weaknesses"]:
            for w in data["weaknesses"]:
                st.markdown(
                    f'<div class="pro-card" style="padding:14px 18px;margin:8px 0;'
                    f'border-left:4px solid #f59e0b;">⚠️ {w}</div>',
                    unsafe_allow_html=True,
                )
        else:
            st.info("See the full feedback for weaknesses")
    
    st.markdown("---")
    
    with st.expander("📄 Full Feedback Report"):
        st.markdown(st.session_state.feedback)
    
    with st.expander(f"📋 Full Transcript ({len(st.session_state.answers)} Q&A)"):
        for i, item in enumerate(st.session_state.answers, 1):
            st.markdown(f"#### Q{i}: {item['question']}")
            st.markdown(f"**Your Answer:**")
            st.write(item["answer"])
            st.markdown(f"**Evaluation:**")
            st.write(item["evaluation"])
            st.markdown("---")
    
    st.markdown("---")
    _, mid, _ = st.columns([1, 1, 1])
    with mid:
        if st.button("🔄 New Interview", type="primary", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()