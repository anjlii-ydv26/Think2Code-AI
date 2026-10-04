
import streamlit as st
import requests
import textwrap

# ============================================================
# THINK2CODE AI — LIGHTWEIGHT STREAMLIT FRONTEND
# ============================================================

API_URL = "http://127.0.0.1:5000"


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Think2Code AI",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# HTML HELPER
# Removes Python indentation so HTML renders correctly.
# ============================================================

def html_block(content):
    st.markdown(
        textwrap.dedent(content),
        unsafe_allow_html=True
    )


# ============================================================
# CUSTOM LIGHT THEME
# ============================================================

st.markdown("""
<style>

    /* -------------------------------------------------------
       GLOBAL
    ------------------------------------------------------- */

    .stApp {
        background: #f8fafc;
        color: #172033;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    /* -------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e2e8f0;
    }

    section[data-testid="stSidebar"] * {
        color: #334155;
    }

    /* -------------------------------------------------------
       HERO
    ------------------------------------------------------- */

    .hero {
        background: linear-gradient(
            135deg,
            #eef2ff 0%,
            #f8fafc 55%,
            #eff6ff 100%
        );

        border: 1px solid #dbe4f0;
        border-radius: 24px;
        padding: 3rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }

    .hero-badge {
        display: inline-block;
        padding: 0.45rem 1rem;
        border-radius: 999px;
        background: #e0e7ff;
        color: #4338ca;
        border: 1px solid #c7d2fe;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.4px;
        margin-bottom: 1rem;
    }

    .hero h1 {
        color: #172554;
        font-size: 3rem;
        line-height: 1.1;
        margin: 0;
        font-weight: 800;
    }

    .hero-subtitle {
        color: #4f46e5;
        font-size: 1.15rem;
        font-weight: 600;
        margin-top: 0.8rem;
    }

    .hero-description {
        max-width: 720px;
        margin: 1rem auto 0 auto;
        color: #64748b;
        line-height: 1.7;
        font-size: 0.98rem;
    }

    /* -------------------------------------------------------
       SECTION TITLES
    ------------------------------------------------------- */

    .section-title {
        color: #172033;
        font-size: 1.3rem;
        font-weight: 750;
        margin-top: 1.8rem;
        margin-bottom: 1rem;
    }

    /* -------------------------------------------------------
       PIPELINE
    ------------------------------------------------------- */

    .pipeline {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.45rem;
        flex-wrap: wrap;
        margin: 1rem 0 2rem 0;
    }

    .pipeline-step {
        padding: 0.65rem 1rem;
        border-radius: 10px;
        background: #ffffff;
        border: 1px solid #dbe3ee;
        color: #334155;
        font-size: 0.86rem;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .pipeline-arrow {
        color: #6366f1;
        font-weight: 700;
        font-size: 1.1rem;
    }

    /* -------------------------------------------------------
       FEATURE CARDS
    ------------------------------------------------------- */

    .feature-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.15rem;
        min-height: 145px;
        margin-bottom: 1rem;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.045);
    }

    .feature-card:hover {
        border-color: #c7d2fe;
    }

    .feature-icon {
        font-size: 1.5rem;
    }

    .feature-title {
        color: #1e293b;
        font-weight: 700;
        margin: 0.4rem 0;
    }

    .feature-text {
        color: #64748b;
        font-size: 0.85rem;
        line-height: 1.5;
    }

    /* -------------------------------------------------------
       RESPONSE BOX
    ------------------------------------------------------- */

    .response-box {
        background: #ffffff;
        border: 1px solid #dbe3ee;
        border-left: 4px solid #6366f1;
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
    }

    /* -------------------------------------------------------
       STATUS
    ------------------------------------------------------- */

    .status-online {
        color: #15803d !important;
        font-weight: 700;
    }

    .status-offline {
        color: #dc2626 !important;
        font-weight: 700;
    }

    /* -------------------------------------------------------
       BUTTONS
    ------------------------------------------------------- */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #c7d2fe;
        background: #eef2ff;
        color: #3730a3;
        font-weight: 650;
        min-height: 42px;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background: #e0e7ff;
        border-color: #818cf8;
        color: #312e81;
    }

    /* -------------------------------------------------------
       TEXT INPUTS
    ------------------------------------------------------- */

    textarea,
    input {
        border-radius: 10px !important;
    }

    /* -------------------------------------------------------
       TABS
    ------------------------------------------------------- */

    button[data-baseweb="tab"] {
        color: #64748b;
        font-weight: 600;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #4f46e5;
    }

    /* -------------------------------------------------------
       FOOTER
    ------------------------------------------------------- */

    .footer {
        text-align: center;
        color: #94a3b8;
        padding: 2rem 0 1rem 0;
        font-size: 0.8rem;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# API FUNCTIONS
# ============================================================

def call_api(endpoint, payload):

    try:

        response = requests.post(
            f"{API_URL}{endpoint}",
            json=payload,
            timeout=180
        )

        if response.status_code == 200:
            return response.json()

        try:
            error_message = response.json().get(
                "error",
                "Backend request failed."
            )
        except Exception:
            error_message = "Backend request failed."

        return {"error": error_message}

    except requests.exceptions.ConnectionError:

        return {
            "error":
            "Think2Code AI backend is not running. "
            "Please start the Flask backend first."
        }

    except requests.exceptions.Timeout:

        return {
            "error":
            "The AI response took too long. Please try again."
        }

    except Exception as e:

        return {"error": str(e)}


def backend_online():

    try:

        response = requests.get(
            f"{API_URL}/health",
            timeout=3
        )

        return response.status_code == 200

    except Exception:

        return False


# ============================================================
# SESSION STATE
# ============================================================

if "problem" not in st.session_state:
    st.session_state.problem = ""

if "understanding" not in st.session_state:
    st.session_state.understanding = None

if "hint_level" not in st.session_state:
    st.session_state.hint_level = 0

if "hints" not in st.session_state:
    st.session_state.hints = []

if "why_line" not in st.session_state:
    st.session_state.why_line = None

if "solution" not in st.session_state:
    st.session_state.solution = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 💡 Think2Code AI")

    st.caption("From Problem to Program")

    st.markdown("---")

    st.markdown("### Learning Path")

    st.markdown("""
**1. Understand**  
Understand what the problem asks.

**2. Think**  
Break the problem into smaller steps.

**3. Practice**  
Use hints and guiding questions.

**4. Construct**  
Build the solution logically.

**5. Solve**  
Review the complete solution.
""")

    st.markdown("---")

    st.markdown("### 🧠 Core Concepts")

    for concept in [
        "Variables",
        "Conditions",
        "Loops",
        "Lists",
        "Functions"
    ]:

        st.markdown(f"• {concept}")

    st.markdown("---")

    if backend_online():

        st.markdown(
            '<span class="status-online">● AI Backend Online</span>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<span class="status-offline">● AI Backend Offline</span>',
            unsafe_allow_html=True
        )


# ============================================================
# HERO
# ============================================================

html_block("""
<div class="hero">

    <div class="hero-badge">
        🧠 AI-POWERED PROGRAMMING LEARNING
    </div>

    <h1>Think2Code AI</h1>

    <div class="hero-subtitle">
        Learn to think. Then learn to code.
    </div>

    <div class="hero-description">
        An interactive programming tutor that helps students understand
        problems, develop logical thinking, use progressive hints,
        and construct solutions step-by-step instead of simply
        receiving the final code.
    </div>

</div>
""")


# ============================================================
# LEARNING PIPELINE
# ============================================================

st.markdown(
    '<div class="section-title">🚀 From Problem to Program</div>',
    unsafe_allow_html=True
)

html_block("""
<div class="pipeline">

    <div class="pipeline-step">Problem</div>
    <div class="pipeline-arrow">→</div>

    <div class="pipeline-step">Understand</div>
    <div class="pipeline-arrow">→</div>

    <div class="pipeline-step">Think</div>
    <div class="pipeline-arrow">→</div>

    <div class="pipeline-step">Hints</div>
    <div class="pipeline-arrow">→</div>

    <div class="pipeline-step">Construct</div>
    <div class="pipeline-arrow">→</div>

    <div class="pipeline-step">Solution</div>

</div>
""")


# ============================================================
# FEATURES
# ============================================================

st.markdown(
    '<div class="section-title">✨ Learning Features</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    html_block("""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Understand</div>
        <div class="feature-text">
            Break the problem down before writing code.
        </div>
    </div>
    """)

with col2:

    html_block("""
    <div class="feature-card">
        <div class="feature-icon">💡</div>
        <div class="feature-title">Progressive Hints</div>
        <div class="feature-text">
            Receive increasingly specific hints when needed.
        </div>
    </div>
    """)

with col3:

    html_block("""
    <div class="feature-card">
        <div class="feature-icon">🧩</div>
        <div class="feature-title">Why This Line?</div>
        <div class="feature-text">
            Understand why individual code lines are needed.
        </div>
    </div>
    """)

with col4:

    html_block("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Final Solution</div>
        <div class="feature-text">
            Review a complete solution after learning the logic.
        </div>
    </div>
    """)


# ============================================================
# PROBLEM INPUT
# ============================================================

st.markdown(
    '<div class="section-title">🎯 Start Learning</div>',
    unsafe_allow_html=True
)

problem = st.text_area(
    "Enter a Python programming problem",
    value=st.session_state.problem,
    placeholder="Example: Find the largest number in a list.",
    height=100
)

st.session_state.problem = problem.strip()

start_col, clear_col = st.columns([3, 1])

with start_col:

    if st.button(
        "🚀 Start Learning",
        use_container_width=True
    ):

        if not st.session_state.problem:

            st.warning(
                "Please enter a programming problem."
            )

        else:

            with st.spinner(
                "Think2Code AI is analyzing the problem..."
            ):

                result = call_api(
                    "/understand",
                    {
                        "problem": st.session_state.problem
                    }
                )

            if "error" in result:

                st.error(result["error"])

            else:

                st.session_state.understanding = result
                st.session_state.hint_level = 0
                st.session_state.hints = []
                st.session_state.why_line = None
                st.session_state.solution = None

                st.success(
                    "Problem analyzed successfully!"
                )


with clear_col:

    if st.button(
        "🗑️ Clear",
        use_container_width=True
    ):

        st.session_state.problem = ""
        st.session_state.understanding = None
        st.session_state.hint_level = 0
        st.session_state.hints = []
        st.session_state.why_line = None
        st.session_state.solution = None

        st.rerun()


# ============================================================
# LEARNING TABS
# ============================================================

if st.session_state.problem:

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔍 Understand",
        "💡 Hint",
        "🧩 Why This Line?",
        "⚡ Final Solution"
    ])


    # ========================================================
    # UNDERSTAND
    # ========================================================

    with tab1:

        st.markdown("### 🔍 Problem Understanding")

        if st.session_state.understanding is None:

            st.info(
                "Click **Start Learning** to begin."
            )

        else:

            answer = st.session_state.understanding.get(
                "answer",
                "No response received."
            )

            html_block("""
            <div class="response-box">
            """)

            st.markdown(answer)

            html_block("""
            </div>
            """)

            st.markdown("### 📚 Retrieved Knowledge")

            contexts = st.session_state.understanding.get(
                "retrieved_context",
                []
            )

            for i, item in enumerate(
                contexts,
                start=1
            ):

                with st.expander(
                    f"Knowledge {i} — {item.get('source', 'Unknown')}"
                ):

                    st.write(
                        item.get("text", "")
                    )


    # ========================================================
    # PROGRESSIVE HINTS
    # ========================================================

    with tab2:

        st.markdown("### 💡 Progressive Hints")

        st.write(
            "Hints become more specific as you progress. "
            "Try solving the problem yourself before revealing "
            "the next hint."
        )

        if st.session_state.hint_level >= 3:

            st.info(
                "You have used all three progressive hints."
            )

        else:

            next_level = (
                st.session_state.hint_level + 1
            )

            if st.button(
                f"💡 Reveal Hint {next_level}",
                key=f"hint_{next_level}",
                use_container_width=True
            ):

                with st.spinner(
                    "Generating hint..."
                ):

                    result = call_api(
                        "/hint",
                        {
                            "problem":
                                st.session_state.problem,
                            "hint_level":
                                next_level
                        }
                    )

                if "error" in result:

                    st.error(result["error"])

                else:

                    st.session_state.hint_level = next_level

                    st.session_state.hints.append(
                        result.get("hint", "")
                    )

            for i, hint in enumerate(
                st.session_state.hints,
                start=1
            ):

                st.markdown(
                    f"**Hint {i}**"
                )

                st.info(hint)


    # ========================================================
    # WHY THIS LINE
    # ========================================================

    with tab3:

        st.markdown("### 🧩 Understand Your Code")

        code_line = st.text_input(
            "Enter one Python code line",
            placeholder="Example: largest = numbers[0]",
            key="why_line_input"
        )

        if st.button(
            "🔎 Explain This Line",
            use_container_width=True
        ):

            if not code_line.strip():

                st.warning(
                    "Please enter a Python code line."
                )

            else:

                with st.spinner(
                    "Explaining the code line..."
                ):

                    result = call_api(
                        "/why-line",
                        {
                            "problem":
                                st.session_state.problem,
                            "code_line":
                                code_line.strip()
                        }
                    )

                if "error" in result:

                    st.error(result["error"])

                else:

                    st.session_state.why_line = result.get(
                        "answer",
                        "No explanation received."
                    )

        if st.session_state.why_line:

            html_block("""
            <div class="response-box">
            """)

            st.markdown(
                st.session_state.why_line
            )

            html_block("""
            </div>
            """)


    # ========================================================
    # FINAL SOLUTION
    # ========================================================

    with tab4:

        st.markdown("### ⚡ Final Solution")

        st.warning(
            "Try understanding the logic and using the hints first. "
            "Reveal the complete solution when you are ready."
        )

        if st.button(
            "⚡ Generate Final Solution",
            use_container_width=True
        ):

            with st.spinner(
                "Generating the final solution..."
            ):

                result = call_api(
                    "/solution",
                    {
                        "problem":
                            st.session_state.problem
                    }
                )

            if "error" in result:

                st.error(result["error"])

            else:

                st.session_state.solution = result.get(
                    "answer",
                    "No solution received."
                )

        if st.session_state.solution:

            html_block("""
            <div class="response-box">
            """)

            st.markdown(
                st.session_state.solution
            )

            html_block("""
            </div>
            """)


# ============================================================
# FOOTER
# ============================================================

html_block("""
<div class="footer">

    Think2Code AI • From Problem to Program 🧠💻

    <br>

    Built as an AI-powered interactive programming
    reasoning and learning platform.

</div>
""")
