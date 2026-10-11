import streamlit as st
from api_client import InterviewAPI
from styles import apply_custom_styles, status_pill

st.set_page_config(
    page_title="AI Interview",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_custom_styles()
api = InterviewAPI()


def init_state():
    defaults = {
        "screen": "setup",
        "session_id": None,
        "resume_text": "",
        "job_description": "",
        "current_question": None,
        "current_index": 0,
        "total_questions": 0,
        "answers": [],
        "feedback": None,
        "is_complete": False,
        "face_frames": [],
        "current_audio": None,
        "last_question_index": -1,
        "spoken_answer": "",
        "last_uploaded_file": None,
        "recording_stage": "idle",   # idle | recording | processing
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()

# Top bar
c1, c2, c3 = st.columns([2, 3, 1])
with c1:
    st.markdown(
        '<h2 style="margin:0; font-size:1.4rem;">🎙️ AI Interview</h2>',
        unsafe_allow_html=True,
    )
with c3:
    if api.health_check():
        st.markdown(status_pill("Live", "ok"), unsafe_allow_html=True)
    else:
        st.markdown(status_pill("Offline", "bad"), unsafe_allow_html=True)

st.markdown("---")

if st.session_state.screen == "setup":
    from components.setup_screen import render
    render(api)
elif st.session_state.screen == "interview":
    from components.interview_screen import render
    render(api)
elif st.session_state.screen == "feedback":
    from components.feedback_screen import render
    render(api)