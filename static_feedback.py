"""
STATIC FEEDBACK PAGE — Video Demo Only
Yeh page sirf video recording ke liye hai. Backend call nahi karta.
Real feedback jaisa dikhta hai — Abhay Patel (Junior AI/ML Engineer) ke liye.
"""

import streamlit as st
from styles import apply_custom_styles, render_score_card, render_badge, render_stars

st.set_page_config(
    page_title="Interview Feedback - Abhay Patel",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_custom_styles()


# ============================================================
# STATIC DATA — Real interview ke liye fixed
# ============================================================

CANDIDATE_NAME = "Abhay Patel"
ROLE = "Junior AI/ML Engineer – Fresher"

INTERVIEW_QA = [
    {
        "question": "Explain the difference between supervised and unsupervised learning. Give one real-world example of each.",
        "answer": "Supervised learning uses labeled data — input ke saath correct output bhi diya jata hai. Model in examples se pattern seekhta hai. Example: spam detection, jahan emails labeled hain 'spam' ya 'not spam'. Unsupervised learning mein labels nahi hote — model khud data mein structure dhoondta hai. Example: customer segmentation, jahan company customers ko groups mein divide karti hai bina pehle se bataye ki kaunsa group kya hai. Maine apne Brain Tumor Detection project mein supervised learning use ki — labeled MRI images se CNN train kiya.",
        "evaluation": "Excellent conceptual clarity. Candidate ne dono concepts clearly differentiate kiye aur real-world examples diye. Brain Tumor project ka reference dena strong point tha — shows hands-on experience. Score: 9/10",
    },
    {
        "question": "What is overfitting in machine learning? How do you prevent it?",
        "answer": "Overfitting tab hota hai jab model training data ko itna yaad kar leta hai ki naye data pe perform nahi karta. Training accuracy high hoti hai lekin validation accuracy low. Prevent karne ke liye main yeh techniques use karta hoon: Dropout layers, regularization (L1/L2), early stopping, aur data augmentation. Apne CNN project mein maine Dropout 0.3 aur early stopping use ki thi — validation accuracy 94% tak gayi.",
        "evaluation": "Strong answer with practical application. Candidate ne classic techniques batayi aur apne project se example bhi diya. Thoda aur depth add kar sakta tha (cross-validation, ensemble methods). Score: 8/10",
    },
    {
        "question": "What is RAG (Retrieval Augmented Generation)? How is it useful in LLM applications?",
        "answer": "RAG ek technique hai jisme LLM ko external knowledge se augment karte hain. Pehle relevant documents ko vector database mein store karte hain (jaise FAISS ya ChromaDB). User query aane pe, similar chunks retrieve karke LLM ko context ke saath dete hain. Isse LLM up-to-date aur domain-specific answers de sakta hai, bina fine-tuning ke. Maine YouTube Video Chatbot project mein RAG use kiya — LangChain + ChromaDB + FAISS ke saath.",
        "evaluation": "Very good — conceptual + practical. Candidate ne RAG ka full pipeline explain kiya aur apne project se validate kiya. Yeh exactly wahi answer hai jo fresher se expected hai. Score: 9/10",
    },
    {
        "question": "Explain your AI Interview Coach project. What challenges did you face?",
        "answer": "AI Interview Coach ek multi-agent system hai jo LangChain aur LangGraph pe bana hai. Isme 4 agents hain — Resume Parser, Job Description Analyzer, Question Generator, aur Feedback Agent. Voice input ke liye Whisper aur ElevenLabs use kiye. Main challenge tha agents ke beech state management — LangGraph se solve kiya. Dusra challenge tha latency — parallel processing aur streaming se improve kiya.",
        "evaluation": "Excellent project explanation. Candidate ne architecture, tech stack, aur specific challenges clearly articulate kiye. State management aur latency jaise advanced issues discuss karna shows maturity. Score: 9/10",
    },
    {
        "question": "Why do you want to work as a Junior AI/ML Engineer? Where do you see yourself in 2 years?",
        "answer": "Mujhe AI/ML mein interest tab se hai jab maine apna first CNN model banaya — Brain Tumor Detection. Uske baad se maine continuous learning kari — LangChain, RAG, LangGraph. Main production-ready AI solutions banana chahta hoon, sirf notebooks tak limited nahi rehna chahta. 2 saal mein main ek strong AI engineer banna chahta hoon jo end-to-end systems design kar sake, aur ideally ek open-source AI project mein contribute karu.",
        "evaluation": "Genuine and well-articulated. Candidate ki passion clearly dikh rahi hai, aur career roadmap realistic hai. 'Production-ready' mindset strong plus point hai. Score: 8.5/10",
    },
]

STRENGTHS = [
    "Strong fundamentals in ML, DL, and Generative AI concepts",
    "Hands-on project experience with LangChain, LangGraph, and RAG pipelines",
    "Ability to connect theory with practical project examples in every answer",
    "Clear and structured communication — explains complex topics simply",
    "Production mindset — focus on deployment, latency, and real-world usage",
]

WEAKNESSES = [
    "Limited exposure to MLOps and model deployment at scale",
    "Could strengthen knowledge of advanced evaluation metrics (F1, ROC-AUC, etc.)",
    "Depth in TensorFlow internals and custom layer design is still developing",
]

OVERALL_SCORE = 8.7
RECOMMENDATION = "Strong Yes"

FACE_STATS = {
    "presence": 96,
    "attention": 8.6,
    "dominant_emotion": "Focused",
    "warnings": 0,
}

SUMMARY = (
    "Abhay Patel demonstrates strong fundamentals and genuine passion for AI/ML. "
    "His project work — especially the AI Interview Coach with LangGraph and RAG-based "
    "YouTube Chatbot — shows he can build production-ready AI applications. "
    "He communicates clearly, connects theory to practice, and has a growth mindset. "
    "Highly recommended for Junior AI/ML Engineer role."
)


# ============================================================
# RENDER
# ============================================================

def render_feedback():
    # Header
    st.markdown(f"## ✅ Interview Complete")
    st.markdown(
        f'<p style="color:#64748b;margin-top:-8px;font-size:1.05rem;">'
        f'<b>{CANDIDATE_NAME}</b> — {ROLE}'
        f'</p>',
        unsafe_allow_html=True,
    )
    
    st.markdown("")
    st.markdown("---")
    
    # ===== TOP: Score + Stars + Recommendation =====
    c1, c2, c3 = st.columns(3)
    
    with c1:
        render_score_card("Overall Score", f"{OVERALL_SCORE}/10", "🎯")
    
    with c2:
        st.markdown(
            '<div class="score-card">'
            '<div style="font-size:1.4rem;">⭐</div>'
            '<div class="score-label">Rating</div>',
            unsafe_allow_html=True,
        )
        render_stars(OVERALL_SCORE)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c3:
        st.markdown(
            '<div class="score-card">'
            '<div style="font-size:1.4rem;">💼</div>'
            '<div class="score-label">Recommendation</div>',
            unsafe_allow_html=True,
        )
        render_badge(RECOMMENDATION)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown("---")
    
    # ===== FACE ANALYSIS =====
    st.markdown("### 📹 Face Analysis Summary")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_score_card("Face Presence", f"{FACE_STATS['presence']}%", "👤")
    with c2:
        render_score_card("Avg Attention", f"{FACE_STATS['attention']}/10", "🎯")
    with c3:
        render_score_card("Emotion", FACE_STATS['dominant_emotion'], "😊")
    with c4:
        render_score_card("Warnings", str(FACE_STATS['warnings']), "⚠️")
    
    st.markdown("---")
    
    # ===== STRENGTHS + WEAKNESSES =====
    c_s, c_w = st.columns(2)
    
    with c_s:
        st.markdown("### ✅ Strengths")
        for s in STRENGTHS:
            st.markdown(
                f'<div class="pro-card" style="padding:14px 18px;margin:8px 0;'
                f'border-left:4px solid #10b981;">✅ {s}</div>',
                unsafe_allow_html=True,
            )
    
    with c_w:
        st.markdown("### ⚠️ Areas to Improve")
        for w in WEAKNESSES:
            st.markdown(
                f'<div class="pro-card" style="padding:14px 18px;margin:8px 0;'
                f'border-left:4px solid #f59e0b;">⚠️ {w}</div>',
                unsafe_allow_html=True,
            )
    
    st.markdown("---")
    
    # ===== FULL FEEDBACK REPORT =====
    st.markdown("### 📄 Full Feedback Report")
    st.markdown(
        f'<div class="pro-card" style="padding:24px;font-size:1rem;line-height:1.7;color:#1e293b;">'
        f'{SUMMARY}'
        f'</div>',
        unsafe_allow_html=True,
    )
    
    st.markdown("---")
    
    # ===== TRANSCRIPT =====
    with st.expander(f"📋 Full Transcript ({len(INTERVIEW_QA)} Q&A)", expanded=False):
        for i, item in enumerate(INTERVIEW_QA, 1):
            st.markdown(f"#### Q{i}: {item['question']}")
            st.markdown(f"**Your Answer:**")
            st.write(item["answer"])
            st.markdown(f"**Evaluation:** {item['evaluation']}")
            st.markdown("---")


if __name__ == "__main__":
    render_feedback()