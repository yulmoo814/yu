import streamlit as st


st.set_page_config(
    page_title="이유리 | 자기소개",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #202820;
        --muted: #687269;
        --green: #527a5d;
        --green-dark: #355440;
        --cream: #f7f8f3;
        --line: #e7ebe3;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 92% 5%, rgba(210, 229, 210, .45), transparent 26rem),
            var(--cream);
        color: var(--ink);
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }

    .block-container {
        max-width: 1040px;
        padding: 3.3rem 2rem 2rem;
    }

    [data-testid="stHeader"], [data-testid="stToolbar"] {
        background: transparent;
    }

    .eyebrow {
        color: var(--green);
        font-size: .78rem;
        font-weight: 700;
        letter-spacing: .2em;
        margin: 0 0 1.1rem;
    }

    .hero-title {
        color: var(--ink);
        font-size: clamp(3.5rem, 9vw, 6.6rem);
        font-weight: 800;
        letter-spacing: -.075em;
        line-height: 1.06;
        margin: 0;
    }

    .hero-title span {
        color: var(--green);
    }

    .hero-copy {
        color: var(--muted);
        font-size: 1.08rem;
        line-height: 1.9;
        margin: 1.35rem 0 0;
    }

    .identity-card {
        align-items: center;
        background: linear-gradient(145deg, #e6efe4, #d9e7d8);
        border: 1px solid rgba(82, 122, 93, .12);
        border-radius: 28px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 300px;
        overflow: hidden;
        position: relative;
        text-align: center;
    }

    .identity-card::before, .identity-card::after {
        border: 1px solid rgba(82, 122, 93, .14);
        border-radius: 50%;
        content: "";
        height: 260px;
        position: absolute;
        width: 260px;
    }

    .identity-card::before {
        right: -128px;
        top: -138px;
    }

    .identity-card::after {
        bottom: -190px;
        left: -90px;
        height: 300px;
        width: 300px;
    }

    .identity-mark {
        align-items: center;
        background: rgba(255, 255, 255, .7);
        border: 1px solid rgba(255, 255, 255, .9);
        border-radius: 50%;
        box-shadow: 0 16px 45px rgba(53, 84, 64, .1);
        color: var(--green-dark);
        display: flex;
        font-size: 2.5rem;
        font-weight: 700;
        height: 116px;
        justify-content: center;
        letter-spacing: -.08em;
        position: relative;
        width: 116px;
        z-index: 1;
    }

    .identity-caption {
        color: var(--green-dark);
        font-size: .78rem;
        font-weight: 700;
        letter-spacing: .18em;
        margin-top: 1.2rem;
        position: relative;
        z-index: 1;
    }

    .section-label {
        color: var(--green);
        font-size: .75rem;
        font-weight: 700;
        letter-spacing: .17em;
        margin: 0 0 .4rem;
    }

    .section-title {
        color: var(--ink);
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -.05em;
        margin: 0 0 1.4rem;
    }

    .profile-card {
        background: rgba(255, 255, 255, .76);
        border: 1px solid var(--line);
        border-radius: 20px;
        height: 100%;
        padding: 1.35rem 1.45rem;
    }

    .profile-label {
        color: #859087;
        font-size: .78rem;
        font-weight: 600;
        margin-bottom: .55rem;
    }

    .profile-value {
        color: var(--ink);
        font-size: 1.1rem;
        font-weight: 700;
    }

    .about-card {
        background: var(--green-dark);
        border-radius: 22px;
        color: #f7faf5;
        padding: 1.7rem 1.9rem;
    }

    .about-card .about-kicker {
        color: #c8ddc8;
        font-size: .75rem;
        font-weight: 700;
        letter-spacing: .16em;
        margin-bottom: .8rem;
    }

    .about-card p {
        color: #f2f6ef;
        font-size: 1rem;
        line-height: 1.9;
        margin: 0;
    }

    .footer {
        border-top: 1px solid var(--line);
        color: #879087;
        font-size: .8rem;
        margin-top: 3.4rem;
        padding-top: 1.2rem;
        text-align: center;
    }

    @media (max-width: 640px) {
        .block-container {
            padding: 2rem 1.15rem 1rem;
        }

        .identity-card {
            min-height: 230px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

hero_copy, hero_art = st.columns([1.25, 0.75], gap="large", vertical_alignment="center")

with hero_copy:
    st.markdown(
        """
        <p class="eyebrow">A LITTLE INTRODUCTION</p>
        <h1 class="hero-title">안녕하세요,<br />이유리<span>입니다.</span></h1>
        <p class="hero-copy">
            경복비즈니스고등학교 3학년,<br />
            IT비즈니스과에서 배우고 있는 이유리입니다.
        </p>
        """,
        unsafe_allow_html=True,
    )

with hero_art:
    st.markdown(
        """
        <div class="identity-card">
            <div class="identity-mark">유리</div>
            <div class="identity-caption">IT BUSINESS</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")

st.markdown(
    """
    <p class="section-label">ABOUT ME</p>
    <h2 class="section-title">저를 소개합니다</h2>
    """,
    unsafe_allow_html=True,
)

profile = st.columns(4, gap="medium")
for column, label, value in zip(
    profile,
    ("이름", "나이", "학교", "전공"),
    ("이유리", "19세", "경복비즈니스고등학교 · 3학년", "IT비즈니스과"),
):
    with column:
        st.markdown(
            f"""
            <div class="profile-card">
                <div class="profile-label">{label}</div>
                <div class="profile-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
st.write("")
st.markdown(
    """
    <div class="about-card">
        <div class="about-kicker">MY SCHOOL LIFE</div>
        <p>
            경복비즈니스고등학교 IT비즈니스과에서 공부하며
            IT와 비즈니스 분야를 함께 배워가고 있습니다.
        </p>
    </div>
    <div class="footer">이유리 · 자기소개</div>
    """,
    unsafe_allow_html=True,
)
