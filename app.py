import streamlit as st
import random

st.set_page_config(page_title="For You", page_icon="💛", layout="centered")

# ── Styling ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400&display=swap');

    html, body, [class*="css"] {
        background-color: #fff8f0;
        font-family: 'Lato', sans-serif;
    }

    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        color: #c0392b;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 1.1rem;
        color: #888;
        text-align: center;
        margin-bottom: 2rem;
    }

    .card {
        background: linear-gradient(135deg, #fff0f0, #fff8f0);
        border: 1.5px solid #f5c6c6;
        border-radius: 20px;
        padding: 2.5rem 2rem;
        text-align: center;
        box-shadow: 0 8px 30px rgba(192,57,43,0.08);
        margin: 1.5rem auto;
        max-width: 520px;
    }

    .card-number {
        font-size: 0.85rem;
        color: #e08080;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    .card-reason {
        font-family: 'Playfair Display', serif;
        font-size: 1.55rem;
        color: #2c2c2c;
        line-height: 1.5;
        margin: 0.5rem 0 1rem;
    }

    .card-emoji {
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
    }

    .progress-label {
        font-size: 0.8rem;
        color: #aaa;
        text-align: center;
        margin-top: 0.5rem;
    }

    .stButton > button {
        background-color: #c0392b;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.55rem 2rem;
        font-size: 1rem;
        font-family: 'Lato', sans-serif;
        letter-spacing: 0.05em;
        cursor: pointer;
        transition: background 0.2s;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #a93226;
    }

    .final-message {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        color: #c0392b;
        text-align: center;
        line-height: 1.8;
        padding: 1rem;
    }

    .heart-divider {
        text-align: center;
        font-size: 1.2rem;
        color: #e08080;
        letter-spacing: 0.4rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Reasons — customize these! ─────────────────────────────────────────────────
REASONS = [
    ("🌅", "The way you make ordinary days feel like adventures"),
    ("😂", "Your laugh — it's the best sound in any room"),
    ("🤝", "How you always show up, without even being asked"),
    ("🌙", "The late-night talks that somehow fix everything"),
    ("💡", "You see the best in me, even when I can't"),
    ("🌸", "Your kindness — it's quiet but it changes everything"),
    ("☕", "The little things you do that you don't even notice"),
    ("🧠", "How smart and thoughtful you are in everything you do"),
    ("🏠", "Being with you feels like being home"),
    ("💛", "Today — for making it feel so incredibly special"),
    ("🎵", "The way you sing and the sound of your voice calms me down "),
    ("👀", "The look you give me that says everything without a single word"),
    ("🎁", "Loving you feels like the best gift I didn't know I needed"),
    ("🌟", "You make me want to be better, every single day"),
    ("🤗", "Your hugs — they fell so warm"),
    ("🦋", "The butterflies — even now, even still, every time"),
    ("🍓", "your eyes - BRIGHTER THAN THE SUN"),
    ("💫", "The fact that out of everywhere and everyone — I get to be yours"),
]

# ── State ──────────────────────────────────────────────────────────────────────
if "index" not in st.session_state:
    st.session_state.index = 0
if "revealed" not in st.session_state:
    st.session_state.revealed = []
if "done" not in st.session_state:
    st.session_state.done = False

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">Just for Samara ❤️ </div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">a few things I never say enough</div>', unsafe_allow_html=True)
st.markdown('<div class="heart-divider">♥ ♥ ♥</div>', unsafe_allow_html=True)

# ── Main content ───────────────────────────────────────────────────────────────
if not st.session_state.done:
    i = st.session_state.index
    emoji, reason = REASONS[i]

    st.markdown(f"""
    <div class="card">
        <div class="card-number">Reason {i + 1} of {len(REASONS)}</div>
        <div class="card-emoji">{emoji}</div>
        <div class="card-reason">"{reason}"</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="progress-label">{i + 1} / {len(REASONS)} revealed</div>', unsafe_allow_html=True)
    st.progress((i + 1) / len(REASONS))
    st.markdown("<br>", unsafe_allow_html=True)

    if i < len(REASONS) - 1:
        if st.button("Next reason →"):
            st.session_state.index += 1
            st.rerun()
    else:
        if st.button("Finish 💛"):
            st.session_state.done = True
            st.rerun()

else:
    st.markdown("""
    <div class="card">
        <div class="card-emoji">💛</div>
        <div class="card-reason">Thank you for today.<br>Thank you for every day.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="final-message">You make everything better just by being you.<br>I love you. ♥</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start over ↺"):
        st.session_state.index = 0
        st.session_state.done = False
        st.rerun()
