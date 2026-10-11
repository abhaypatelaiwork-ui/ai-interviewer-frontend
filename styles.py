import streamlit as st


def apply_custom_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: #f8fafc;
        color: #0f172a;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    h1 { color: #0f172a !important; font-weight: 800 !important; letter-spacing: -0.03em !important; }
    h2 { color: #1e293b !important; font-weight: 700 !important; letter-spacing: -0.02em !important; }
    h3 { color: #334155 !important; font-weight: 600 !important; font-size: 1.1rem !important; }
    
    .pro-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04), 0 4px 12px rgba(15, 23, 42, 0.03);
        margin-bottom: 16px;
    }
    
    .question-box {
        background: linear-gradient(135deg, #eef2ff 0%, #e0e7ff 100%);
        border-left: 4px solid #4f46e5;
        border-radius: 14px;
        padding: 24px 28px;
        margin: 16px 0 24px 0;
        color: #1e1b4b;
        font-size: 1.15rem;
        line-height: 1.65;
        font-weight: 500;
        box-shadow: 0 2px 12px rgba(79, 70, 229, 0.08);
    }
    
    .metric-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 18px;
    }
    
    .metric-label {
        color: #64748b;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 4px;
    }
    
    .metric-value {
        color: #0f172a;
        font-size: 1.5rem;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    
    .cv-panel {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border: 1px solid #bbf7d0;
        border-radius: 14px;
        padding: 20px;
        margin-top: 16px;
    }
    .cv-panel.warn { background: linear-gradient(135deg, #fefce8 0%, #fef9c3 100%); border-color: #fde047; }
    .cv-panel.danger { background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); border-color: #fecaca; }
    
    .stButton > button {
        background: #4f46e5;
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 14px 28px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.15s ease;
        box-shadow: 0 1px 2px rgba(79, 70, 229, 0.15), 0 4px 12px rgba(79, 70, 229, 0.15);
    }
    .stButton > button:hover {
        background: #4338ca;
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(79, 70, 229, 0.25);
    }
    .stButton > button:disabled { background: #e2e8f0; color: #94a3b8; box-shadow: none; }
    
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        border-radius: 8px;
    }
    .stProgress > div > div > div { background: #e2e8f0; border-radius: 8px; }
    
    .stTextArea textarea, .stTextInput input {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 10px !important;
        color: #0f172a !important;
        font-size: 0.95rem !important;
    }
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #4f46e5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: #f1f5f9;
        padding: 4px;
        border-radius: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: #64748b;
        padding: 10px 20px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: #ffffff !important;
        color: #4f46e5 !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08);
    }
    
    .stAlert { border-radius: 10px; border: 1px solid #e2e8f0; background: #ffffff; }
    
    .score-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    }
    .score-label {
        color: #64748b;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    .score-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #4f46e5;
        margin-top: 8px;
        letter-spacing: -0.03em;
    }
    .stars { font-size: 1.6rem; color: #f59e0b; letter-spacing: 2px; margin-top: 6px; }
    
    .badge {
        display: inline-block;
        padding: 8px 20px;
        border-radius: 24px;
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 0.03em;
        margin-top: 8px;
    }
    .badge-strong { background: #dcfce7; color: #166534; }
    .badge-yes { background: #dbeafe; color: #1e40af; }
    .badge-maybe { background: #fef9c3; color: #854d0e; }
    .badge-no { background: #fee2e2; color: #991b1b; }
    
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
    }
    .status-ok { background: #dcfce7; color: #166534; }
    .status-bad { background: #fee2e2; color: #991b1b; }
    .status-warn { background: #fef9c3; color: #854d0e; }
    
    /* ============================================
       WAVEFORM ANIMATIONS
       ============================================ */
    
    /* Idle state — soft bars */
    .waveform-idle {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 4px;
        height: 60px;
        padding: 8px 0;
    }
    .waveform-idle span {
        width: 5px;
        background: #cbd5e1;
        border-radius: 3px;
        height: 12px;
    }
    
    /* Recording state — animated bars (matching the image) */
    .waveform-recording {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 5px;
        height: 80px;
        padding: 12px 0;
    }
    .waveform-recording span {
        width: 6px;
        background: linear-gradient(180deg, #6366f1, #4f46e5);
        border-radius: 4px;
        box-shadow: 0 0 12px rgba(99, 102, 241, 0.4);
        animation: waveUp 1.2s ease-in-out infinite;
    }
    .waveform-recording span:nth-child(1) { animation-delay: 0s;    height: 20px; }
    .waveform-recording span:nth-child(2) { animation-delay: 0.1s;  height: 30px; }
    .waveform-recording span:nth-child(3) { animation-delay: 0.2s;  height: 24px; }
    .waveform-recording span:nth-child(4) { animation-delay: 0.3s;  height: 40px; }
    .waveform-recording span:nth-child(5) { animation-delay: 0.4s;  height: 34px; }
    .waveform-recording span:nth-child(6) { animation-delay: 0.5s;  height: 46px; }
    .waveform-recording span:nth-child(7) { animation-delay: 0.6s;  height: 56px; }
    
    @keyframes waveUp {
        0%, 100% { transform: scaleY(0.5); opacity: 0.7; }
        50% { transform: scaleY(1.2); opacity: 1; }
    }
    
    /* Speaking state — for question TTS playback */
    .waveform-speaking {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 4px;
        height: 50px;
        padding: 8px 0;
    }
    .waveform-speaking span {
        width: 5px;
        background: linear-gradient(180deg, #818cf8, #6366f1);
        border-radius: 3px;
        animation: waveSpeak 0.9s ease-in-out infinite;
    }
    .waveform-speaking span:nth-child(1) { animation-delay: 0s; }
    .waveform-speaking span:nth-child(2) { animation-delay: 0.08s; }
    .waveform-speaking span:nth-child(3) { animation-delay: 0.16s; }
    .waveform-speaking span:nth-child(4) { animation-delay: 0.24s; }
    .waveform-speaking span:nth-child(5) { animation-delay: 0.32s; }
    .waveform-speaking span:nth-child(6) { animation-delay: 0.4s; }
    .waveform-speaking span:nth-child(7) { animation-delay: 0.48s; }
    .waveform-speaking span:nth-child(8) { animation-delay: 0.56s; }
    .waveform-speaking span:nth-child(9) { animation-delay: 0.64s; }
    
    @keyframes waveSpeak {
        0%, 100% { height: 8px; opacity: 0.6; }
        50% { height: 36px; opacity: 1; }
    }
    
    /* Thinking state — for processing */
    .waveform-thinking {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        height: 60px;
    }
    .waveform-thinking span {
        width: 10px;
        height: 10px;
        background: #4f46e5;
        border-radius: 50%;
        animation: bounce 1.4s ease-in-out infinite;
    }
    .waveform-thinking span:nth-child(1) { animation-delay: 0s; }
    .waveform-thinking span:nth-child(2) { animation-delay: 0.2s; }
    .waveform-thinking span:nth-child(3) { animation-delay: 0.4s; }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); opacity: 0.4; }
        50% { transform: translateY(-16px); opacity: 1; }
    }
    
    /* Recording status header */
    .rec-header {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        font-size: 0.95rem;
        font-weight: 600;
        color: #4f46e5;
        margin-bottom: 4px;
    }
    
    .rec-dot {
        width: 10px;
        height: 10px;
        background: #dc2626;
        border-radius: 50%;
        animation: recPulse 1.4s ease-in-out infinite;
    }
    
    @keyframes recPulse {
        0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.5); }
        50% { opacity: 0.7; transform: scale(1.1); box-shadow: 0 0 0 8px rgba(220, 38, 38, 0); }
    }
    
    .success-pulse {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        color: #16a34a;
        font-weight: 600;
        font-size: 0.95rem;
    }
    .success-pulse::before {
        content: "✓";
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        background: #dcfce7;
        border-radius: 50%;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)


def status_pill(text: str, kind: str = "ok"):
    return f'<span class="status-pill status-{kind}">● {text}</span>'


def render_score_card(label: str, value: str, icon: str = "", color: str = "#4f46e5"):
    st.markdown(f"""
    <div class="score-card">
        <div style="font-size: 1.4rem;">{icon}</div>
        <div class="score-label">{label}</div>
        <div class="score-value" style="color:{color};">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def render_stars(score: float, max_score: float = 10.0):
    filled = round((score / max_score) * 5)
    stars = "★" * filled + "☆" * (5 - filled)
    st.markdown(f'<div class="stars">{stars}</div>', unsafe_allow_html=True)


def render_badge(recommendation: str):
    rec = recommendation.lower()
    if "strong" in rec and "yes" in rec:
        cls, text = "badge-strong", "🌟 Strong Yes"
    elif "yes" in rec:
        cls, text = "badge-yes", "✅ Yes"
    elif "maybe" in rec:
        cls, text = "badge-maybe", "⚠️ Maybe"
    else:
        cls, text = "badge-no", "❌ No"
    st.markdown(
        f'<div style="text-align:center;"><span class="badge {cls}">{text}</span></div>',
        unsafe_allow_html=True,
    )


# ============================================
# WAVEFORM COMPONENTS
# ============================================

def render_idle_waveform():
    """Idle — waiting for user to start."""
    bars = "".join(["<span></span>" for _ in range(7)])
    st.markdown(
        f'<div class="waveform-idle">{bars}</div>',
        unsafe_allow_html=True,
    )


def render_recording_waveform():
    """Recording — animated bars, exactly like the reference image."""
    bars = "".join(["<span></span>" for _ in range(7)])
    st.markdown(
        f'<div class="waveform-recording">{bars}</div>',
        unsafe_allow_html=True,
    )


def render_speaking_waveform():
    """Speaking — for question TTS playback."""
    bars = "".join(["<span></span>" for _ in range(9)])
    st.markdown(
        f'<div class="waveform-speaking">{bars}</div>',
        unsafe_allow_html=True,
    )


def render_thinking_waveform():
    """Thinking — 3 bouncing dots for processing."""
    bars = "".join(["<span></span>" for _ in range(3)])
    st.markdown(
        f'<div class="waveform-thinking">{bars}</div>',
        unsafe_allow_html=True,
    )


def render_recording_header(text: str = "Listening..."):
    st.markdown(
        f'<div class="rec-header"><span class="rec-dot"></span>{text}</div>',
        unsafe_allow_html=True,
    )


def render_success_header(text: str = "Answer captured"):
    st.markdown(
        f'<div class="success-pulse">{text}</div>',
        unsafe_allow_html=True,
    )