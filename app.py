import streamlit as st
import random

st.set_page_config(
    page_title="Neon Tic-Tac-Toe",
    page_icon="🎮",
    layout="centered"
)

# =========================
# NEON + 3D ANIMATION CSS
# =========================
st.markdown(r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800;900&family=Inter:wght@400;600;700;800&display=swap');

:root {
    --cyan: #00F5FF;
    --pink: #FF3CAC;
    --purple: #8B5CF6;
}

.stApp {
    background:
        radial-gradient(ellipse at 12% 15%, #10294C 0%, transparent 42%),
        radial-gradient(ellipse at 88% 80%, #35103F 0%, transparent 45%),
        #050711;
    color: white;
    font-family: 'Inter', sans-serif;
    overflow-x: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 780px;
    padding-top: 1.5rem;
    padding-bottom: 2.5rem;
}

/* Floating 3D symbols */
.stApp::before,
.stApp::after {
    position: fixed;
    z-index: 0;
    pointer-events: none;
    white-space: pre-wrap;
    width: 100%;
    height: 100%;
    font-family: 'Orbitron', sans-serif;
    font-weight: 900;
    line-height: 2.0;
    overflow-wrap: anywhere;
    text-shadow: 0 0 18px currentColor, 0 0 38px currentColor;
}

.stApp::before {
    content: "✕      ○       ✕\A    ○       ✕       ○\A ✕       ○       ✕";
    top: 0;
    left: 0;
    font-size: clamp(35px, 6vw, 75px);
    letter-spacing: 4vw;
    color: var(--cyan);
    opacity: .09;
    animation: drift3D 13s ease-in-out infinite alternate;
}

.stApp::after {
    content: "○      ✕       ○\A   ✕       ○       ✕\A ○       ✕       ○";
    right: 0;
    bottom: -20%;
    font-size: clamp(30px, 5vw, 65px);
    letter-spacing: 3vw;
    color: var(--pink);
    opacity: .08;
    animation: driftPink 17s ease-in-out infinite alternate;
}

@keyframes drift3D {
    0% { transform: translate3d(-2%, -2%, 0) rotateX(0deg) rotateY(-8deg); }
    50% { transform: translate3d(3%, 2%, 0) rotateX(15deg) rotateY(8deg); }
    100% { transform: translate3d(-1%, 5%, 0) rotateX(-10deg) rotateY(-4deg); }
}

@keyframes driftPink {
    0% { transform: translate3d(2%, 3%, 0) rotateY(10deg); }
    100% { transform: translate3d(-3%, -6%, 0) rotateY(-10deg); }
}

/* Header */
.hero {
    text-align: center;
    padding: 12px 0 22px;
    position: relative;
    z-index: 1;
}

.eyebrow {
    color: var(--cyan);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 5px;
}

.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(32px, 6vw, 54px);
    font-weight: 900;
    margin: 12px 0;
    color: white;
    text-shadow: 0 0 22px #00F5FF40;
}

.hero h1 span {
    color: var(--cyan);
    text-shadow: 0 0 25px #00F5FF90;
}

.subtitle {
    color: #C4CBE0;
    font-size: 13px;
    letter-spacing: 2px;
}

/* Player cards */
.player-card {
    background: linear-gradient(145deg, #18243B, #0D1323);
    border: 1px solid #405174;
    border-radius: 18px;
    padding: 14px 8px;
    text-align: center;
    margin-bottom: 15px;
    box-shadow: 0 7px 0 #03050C, 0 0 16px #0005;
}

.player-x, .player-o {
    font-family: 'Orbitron', sans-serif;
    font-size: 36px;
    font-weight: 900;
}

.player-x {
    color: var(--cyan);
    text-shadow: 0 0 22px #00F5FF;
}

.player-o {
    color: var(--pink);
    text-shadow: 0 0 22px #FF3CAC;
}

.player-caption {
    color: #C5D0E9;
    font-size: 12px;
    margin-top: 5px;
}

/* Scoreboard */
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #17243E, #0C1325);
    border: 1px solid #425477;
    border-radius: 16px;
    padding: 12px;
    box-shadow: 0 6px 0 #03050C;
}

div[data-testid="stMetricLabel"] {
    color: #DCE6FF !important;
    font-weight: 700;
}

div[data-testid="stMetricValue"] {
    color: white !important;
    font-family: 'Orbitron', sans-serif;
    font-weight: 900;
}

/* Game buttons */
.stButton > button {
    min-height: 78px;
    width: 100%;
    border: 1px solid #3D4D70;
    border-radius: 15px;
    color: white !important;
    background: linear-gradient(145deg, #202E4B, #10182C);
    font-family: 'Orbitron', sans-serif;
    font-size: 30px;
    font-weight: 900;
    box-shadow: 0 6px 0 #070A14, 0 10px 20px #0005;
    transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}

.stButton > button:hover:not(:disabled) {
    border-color: var(--cyan);
    color: var(--cyan) !important;
    transform: translateY(-3px);
    box-shadow: 0 0 22px #00F5FF50, 0 6px 0 #070A14;
}

.stButton > button:disabled {
    opacity: 1 !important;
    color: white !important;
    -webkit-text-fill-color: white !important;
    background: linear-gradient(145deg, #1B2943, #11182B);
    border-color: #3B4D70;
}

/* Winner panel */
.status-card {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #101D35, #141126);
    border: 1px solid #465B81;
    border-radius: 18px;
    padding: 20px 10px;
    text-align: center;
    margin: 14px 0 20px;
    box-shadow: 0 0 25px #0006;
}

.status-value {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(15px, 3vw, 23px);
    font-weight: 900;
    line-height: 1.6;
    overflow-wrap: anywhere;
}

.winner {
    animation: winnerPulse 0.8s ease-in-out infinite alternate;
}

@keyframes winnerPulse {
    from { text-shadow: 0 0 8px currentColor; transform: scale(1); }
    to { text-shadow: 0 0 28px currentColor, 0 0 45px currentColor; transform: scale(1.025); }
}

/* CSS fireworks on victory */
.firework {
    position: relative;
    height: 95px;
    margin: 0 auto 8px;
    max-width: 440px;
    overflow: hidden;
    pointer-events: none;
}

.burst {
    position: absolute;
    top: 48%;
    left: 50%;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: transparent;
    box-shadow:
        0 -35px #00F5FF, 0 35px #FF3CAC,
        35px 0 #FFD166, -35px 0 #8B5CF6,
        25px 25px #00F5FF, -25px -25px #FF3CAC,
        25px -25px #FFD166, -25px 25px #8B5CF6,
        0 -48px #FF3CAC, 0 48px #00F5FF,
        48px 0 #8B5CF6, -48px 0 #FFD166;
    animation: explode 1.3s ease-out infinite;
}

.burst.two {
    left: 22%;
    top: 52%;
    animation-delay: .4s;
}

.burst.three {
    left: 78%;
    top: 52%;
    animation-delay: .7s;
}

@keyframes explode {
    0% { transform: scale(.12) rotate(0deg); opacity: 0; }
    25% { opacity: 1; }
    100% { transform: scale(1.25) rotate(45deg); opacity: 0; }
}

/* Small confetti-like particles */
.confetti {
    position: absolute;
    width: 7px;
    height: 12px;
    background: var(--cyan);
    top: -15px;
    left: 15%;
    animation: confettiFall 2.5s linear infinite;
}

.confetti:nth-child(2) { left: 35%; background: var(--pink); animation-delay: .3s; }
.confetti:nth-child(3) { left: 55%; background: #FFD166; animation-delay: .8s; }
.confetti:nth-child(4) { left: 75%; background: var(--purple); animation-delay: .5s; }
.confetti:nth-child(5) { left: 90%; background: var(--cyan); animation-delay: 1s; }

@keyframes confettiFall {
    0% { transform: translateY(-10px) rotate(0deg); opacity: 0; }
    15% { opacity: 1; }
    100% { transform: translateY(110px) rotate(360deg); opacity: 0; }
}

.tip {
    color: #D0D9EF;
    font-size: 12px;
    line-height: 1.8;
    text-align: center;
    padding-top: 14px;
}

@media (max-width: 640px) {
    .block-container { padding: 1rem .5rem 2rem; }
    .stButton > button { min-height: 60px; font-size: 23px; padding: 0 2px; }
    div[data-testid="stMetric"] { padding: 9px 4px; }
    div[data-testid="stMetricValue"] { font-size: 22px !important; }
    .player-x, .player-o { font-size: 29px; }
}

@media (prefers-reduced-motion: reduce) {
    .stApp::before, .stApp::after, .winner, .burst, .confetti {
        animation: none !important;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================
# GAME LOGIC
# =========================
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def init_game():
    st.session_state.board = [0] * 9
    st.session_state.current = 1
    st.session_state.result = None
    st.session_state.celebrate = False


def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != 0 and board[a] == board[b] == board[c]:
            return "X" if board[a] == 1 else "O"

    if all(cell != 0 for cell in board):
        return "DRAW"

    return None


def play_move(index):
    if st.session_state.result is not None:
        return

    if st.session_state.board[index] != 0:
        return

    st.session_state.board[index] = st.session_state.current
    result = check_winner(st.session_state.board)

    if result:
        st.session_state.result = result
        st.session_state.scores[result] += 1

        if result in ("X", "O"):
            st.session_state.celebrate = True
    else:
        st.session_state.current *= -1


# =========================
# INITIAL STATE
# =========================
if "board" not in st.session_state:
    init_game()

if "scores" not in st.session_state:
    st.session_state.scores = {"X": 0, "O": 0, "DRAW": 0}


# =========================
# HEADER
# =========================
st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ NEON ARCADE • TWO PLAYER ✦</div>
    <h1>TIC-TAC-<span>TOE</span></h1>
    <div class="subtitle">THINK &nbsp; • &nbsp; PLAY &nbsp; • &nbsp; WIN</div>
</div>
""", unsafe_allow_html=True)


# =========================
# PLAYERS
# =========================
p1, p2 = st.columns(2)

with p1:
    st.markdown("""
    <div class="player-card">
        <div class="player-x">✕</div>
        <b>PLAYER X</b>
        <div class="player-caption">Cyan Player</div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="player-card">
        <div class="player-o">○</div>
        <b>PLAYER O</b>
        <div class="player-caption">Pink Player</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# SCOREBOARD
# =========================
st.markdown(
    "<p style='text-align:center;letter-spacing:3px;"
    "color:#C4CBE0;font-size:12px;'>MATCH SCORE</p>",
    unsafe_allow_html=True
)

s1, s2, s3 = st.columns(3)

with s1:
    st.metric("✕ X WINS", st.session_state.scores["X"])

with s2:
    st.metric("○ O WINS", st.session_state.scores["O"])

with s3:
    st.metric("DRAW", st.session_state.scores["DRAW"])


# =========================
# STATUS + WIN CELEBRATION
# =========================
result = st.session_state.result

if result == "X":
    status = "🏆 PLAYER X WINS!"
    color = "#00F5FF"
elif result == "O":
    status = "🏆 PLAYER O WINS!"
    color = "#FF3CAC"
elif result == "DRAW":
    status = "🤝 MATCH DRAW!"
    color = "#B69CFF"
elif st.session_state.current == 1:
    status = "✕ PLAYER X — YOUR TURN"
    color = "#00F5FF"
else:
    status = "○ PLAYER O — YOUR TURN"
    color = "#FF3CAC"

if result in ("X", "O"):
    st.markdown("""
    <div class="firework">
        <span class="burst"></span>
        <span class="burst two"></span>
        <span class="burst three"></span>
        <span class="confetti"></span>
        <span class="confetti"></span>
        <span class="confetti"></span>
        <span class="confetti"></span>
        <span class="confetti"></span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="status-card">'
        f'<div class="status-value winner" style="color:{color};">'
        f'🎉 {status} 🎉</div>'
        f'<div style="color:#D0D9EF;margin-top:8px;">'
        f'LEGENDARY MOVE! • VICTORY UNLOCKED</div></div>',
        unsafe_allow_html=True
    )

    # Streamlit's built-in celebration animation
    if st.session_state.celebrate:
        st.balloons()
        st.snow()
        st.session_state.celebrate = False

elif result == "DRAW":
    st.markdown(
        f'<div class="status-card"><div class="status-value" '
        f'style="color:{color};">{status}</div></div>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f'<div class="status-card"><div class="status-value" '
        f'style="color:{color};">{status}</div></div>',
        unsafe_allow_html=True
    )


# =========================
# GAME BOARD
# =========================
for row in range(3):
    cols = st.columns(3, gap="small")

    for col in range(3):
        index = row * 3 + col
        value = st.session_state.board[index]

        if value == 1:
            label = "✕"
        elif value == -1:
            label = "○"
        else:
            label = "·"

        with cols[col]:
            st.button(
                label,
                key=f"cell_{index}",
                use_container_width=True,
                disabled=(
                    value != 0 or
                    st.session_state.result is not None
                ),
                on_click=play_move,
                args=(index,)
            )


# =========================
# CONTROLS
# =========================
st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    if st.button("🔄  NEW GAME", use_container_width=True):
        init_game()
        st.rerun()

with c2:
    if st.button("🗑️  RESET SCORE", use_container_width=True):
        st.session_state.scores = {"X": 0, "O": 0, "DRAW": 0}
        init_game()
        st.rerun()

st.markdown("""
<div class="tip">
    💡 Take turns placing X and O. First player to get 3 in a row wins!
    <br>✨ Win to trigger the celebration • Occupied cells stay locked.
</div>
""", unsafe_allow_html=True)