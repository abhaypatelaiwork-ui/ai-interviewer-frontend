import streamlit as st


def render(api):
    st.markdown("## Setup")
    st.markdown(
        '<p style="color:#64748b; margin-top:-8px;">Please provide your resume and job description — we will begin the interview</p>',
        unsafe_allow_html=True,
    )
    
    st.markdown("")
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 📄 Resume")
        
        method = st.radio(
            "Method",
            ["Upload PDF", "Paste Text"],
            horizontal=True,
            label_visibility="collapsed",
        )
        
        if method == "Upload PDF":
            uploaded = st.file_uploader(
                "Resume",
                type=["pdf"],
                label_visibility="collapsed",
            )
            if uploaded:
                file_key = f"{uploaded.name}_{uploaded.size}"
                if st.session_state.last_uploaded_file != file_key:
                    with st.spinner("Extracting text..."):
                        try:
                            result = api.upload_resume(uploaded)
                            st.session_state.resume_text = result["extracted_text"]
                            st.session_state.last_uploaded_file = file_key
                            st.rerun()
                        except Exception as e:
                            st.error(f"Extraction failed: {e}")
            
            if st.session_state.resume_text:
                st.success(f"✅ {len(st.session_state.resume_text)} characters ready")
        else:
            st.session_state.resume_text = st.text_area(
                "Resume",
                value=st.session_state.resume_text,
                height=280,
                label_visibility="collapsed",
                placeholder="Paste resume text...",
            )
    
    with col2:
        st.markdown("### 💼 Job Description")
        st.session_state.job_description = st.text_area(
            "JD",
            value=st.session_state.job_description,
            height=340,
            label_visibility="collapsed",
            placeholder="Paste job description...",
        )
    
    st.markdown("")
    st.markdown("---")
    
    can_start = bool(
        st.session_state.resume_text.strip() and st.session_state.job_description.strip()
    )
    
    _, mid, _ = st.columns([1, 1, 1])
    with mid:
        if st.button(
            "🚀 Start Interview",
            type="primary",
            disabled=not can_start,
            use_container_width=True,
        ):
            _start(api)


def _start(api):
    with st.spinner("Preparing questions..."):
        try:
            r = api.start_interview(
                st.session_state.resume_text,
                st.session_state.job_description,
            )
            st.session_state.session_id = r["session_id"]
            st.session_state.current_question = r["first_question"]
            st.session_state.total_questions = r["total_questions"]
            st.session_state.current_index = 0
            st.session_state.answers = []
            st.session_state.face_frames = []
            st.session_state.screen = "interview"
            st.rerun()
        except Exception as e:
            st.error(f"Failed to start interview: {e}")