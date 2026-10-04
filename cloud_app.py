
import os

# Use the smaller model for Streamlit Community Cloud.
os.environ["THINK2CODE_MODEL"] = "Qwen/Qwen2.5-0.5B-Instruct"

import streamlit as st

from backend import (
    think2code_rag,
    generate_progressive_hint,
    explain_code_line,
    generate_final_solution
)

st.set_page_config(
    page_title="Think2Code AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------------------------------------------------
# Custom styling
# ---------------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: #f8fafc;
}

.hero {
    padding: 2rem 2rem 1.5rem 2rem;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    margin-bottom: 1.5rem;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: #eef2ff;
    color: #4f46e5;
    font-size: 0.8rem;
    font-weight: 700;
    margin-bottom: 10px;
}

.hero h1 {
    font-size: 2.5rem;
    margin-bottom: 0.4rem;
    color: #0f172a;
}

.hero p {
    color: #475569;
    font-size: 1.05rem;
}

.feature-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.2rem;
    height: 100%;
}

.feature-card h3 {
    color: #0f172a;
    margin-bottom: 0.4rem;
}

.feature-card p {
    color: #64748b;
    font-size: 0.92rem;
}

.section-title {
    color: #0f172a;
    font-weight: 700;
    font-size: 1.4rem;
    margin-top: 1.5rem;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Hero
# ---------------------------------------------------------

st.markdown("""
<div class="hero">

<div class="badge">🧠 AI-POWERED PROGRAMMING LEARNING</div>

<h1>Think2Code AI</h1>

<p>
Learn to think. Then learn to code.
</p>

<p>
An interactive programming reasoning platform that guides
students from problem understanding to solution construction
using RAG and a local language model.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Learning pipeline
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Learning Pipeline</div>',
    unsafe_allow_html=True
)

cols = st.columns(6)

pipeline = [
    ("1", "Understand"),
    ("2", "Break Down"),
    ("3", "Concept"),
    ("4", "Hint"),
    ("5", "Construct"),
    ("6", "Solve")
]

for col, (number, label) in zip(cols, pipeline):
    with col:
        st.markdown(
            f"""
            <div class="feature-card" style="text-align:center;">
                <h3>{number}</h3>
                <p>{label}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# Features
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">What Think2Code AI Provides</div>',
    unsafe_allow_html=True
)

feature_cols = st.columns(4)

features = [
    (
        "🔍",
        "Problem Understanding",
        "Break programming problems into understandable reasoning steps."
    ),
    (
        "💡",
        "Progressive Hints",
        "Receive increasingly specific hints without immediately revealing the answer."
    ),
    (
        "📖",
        "Why This Line?",
        "Understand what a Python line does and why it is needed."
    ),
    (
        "⚡",
        "Final Solution",
        "Generate and explain a complete solution after learning the reasoning."
    )
]

for col, (icon, title, description) in zip(feature_cols, features):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <h3>{icon} {title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# Problem input
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Try Think2Code AI</div>',
    unsafe_allow_html=True
)

problem = st.text_area(
    "Enter a Python programming problem",
    value="Find the largest number in a list.",
    height=100,
    placeholder="Example: Check whether a number is prime."
)


if problem.strip():

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🧠 Understand",
            "💡 Hint",
            "🔎 Why This Line?",
            "⚡ Final Solution"
        ]
    )

    # -----------------------------------------------------
    # Understand
    # -----------------------------------------------------

    with tab1:

        if st.button(
            "Understand the Problem",
            type="primary",
            key="understand"
        ):

            with st.spinner("Thinking through the problem..."):

                try:
                    result = think2code_rag(problem)

                    st.session_state["understanding"] = result["answer"]

                except Exception as e:
                    st.error(f"Unable to generate response: {e}")

        if "understanding" in st.session_state:

            st.markdown(st.session_state["understanding"])


    # -----------------------------------------------------
    # Progressive Hint
    # -----------------------------------------------------

    with tab2:

        if "hint_level" not in st.session_state:
            st.session_state["hint_level"] = 0

        st.write(
            f"Hint level: {st.session_state['hint_level']} / 3"
        )

        if st.button(
            "Get Next Hint",
            key="hint"
        ):

            if st.session_state["hint_level"] < 3:

                st.session_state["hint_level"] += 1

                with st.spinner("Preparing your hint..."):

                    try:
                        hint = generate_progressive_hint(
                            problem,
                            st.session_state["hint_level"]
                        )

                        st.session_state["current_hint"] = hint

                    except Exception as e:
                        st.error(f"Unable to generate hint: {e}")

            else:

                st.info(
                    "You have used all three hints. "
                    "Try applying what you learned."
                )

        if "current_hint" in st.session_state:

            st.info(st.session_state["current_hint"])


    # -----------------------------------------------------
    # Why This Line?
    # -----------------------------------------------------

    with tab3:

        code_line = st.text_input(
            "Enter a Python code line",
            placeholder="Example: largest = numbers[0]"
        )

        if st.button(
            "Explain This Line",
            key="why_line"
        ):

            if not code_line.strip():

                st.warning("Please enter a Python code line.")

            else:

                with st.spinner("Explaining the line..."):

                    try:

                        explanation = explain_code_line(
                            problem,
                            code_line
                        )

                        st.markdown(explanation)

                    except Exception as e:

                        st.error(
                            f"Unable to explain the line: {e}"
                        )


    # -----------------------------------------------------
    # Final Solution
    # -----------------------------------------------------

    with tab4:

        st.warning(
            "Try the reasoning and hints first. "
            "The final solution reveals the complete program."
        )

        if st.button(
            "Generate Final Solution",
            key="solution"
        ):

            with st.spinner(
                "Generating the complete solution..."
            ):

                try:

                    result = generate_final_solution(problem)

                    st.markdown(result["answer"])

                except Exception as e:

                    st.error(
                        f"Unable to generate solution: {e}"
                    )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown(
    """
    <br>
    <hr>
    <p style="text-align:center;color:#64748b;">
    Think2Code AI · RAG + Local LLM · Built for interactive programming learning
    </p>
    """,
    unsafe_allow_html=True
)
