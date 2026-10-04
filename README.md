# Think2Code AI

## 🚀 Live Demo

Try Think2Code AI directly in your browser:

[![Open Live Demo](https://img.shields.io/badge/🚀_Try_Live_Demo-Think2Code_AI-FF4B4B?style=for-the-badge)](https://think2code-ai-development.streamlit.app/)

No installation required. Explore problem understanding, progressive hints,
code-line explanations, and final solution generation.
## An AI-Powered Interactive Programming Reasoning and Learning Platform

> From Problem to Program — Learn to think before you code.

Think2Code AI is an AI-powered programming learning platform designed to help beginners understand the reasoning behind programming solutions instead of immediately receiving complete code.

The system combines Retrieval-Augmented Generation (RAG), a local Large Language Model (LLM), and an interactive learning workflow to guide students from problem understanding to solution construction.

---

## Core Principle

Traditional coding assistants often follow:

**Problem → AI → Complete Code**

Think2Code AI follows:

**Problem → Understanding → Decomposition → Concepts → Hints → Code Construction → Explanation → Solution**

The goal is to make students active participants in the problem-solving process.

---

## Key Features

### 1. Problem Understanding

The system explains what the programming problem is asking and identifies the important programming concepts involved.

### 2. RAG-Based Knowledge Retrieval

Relevant programming concepts are retrieved from a curated educational knowledge base using:

- Sentence Transformers
- FAISS vector search
- Semantic similarity

### 3. Progressive Hints

Students receive progressively stronger hints:

- Level 1 — Conceptual clue
- Level 2 — Logical clue
- Level 3 — Implementation clue

Hints become more specific without immediately revealing the complete solution.

### 4. Why This Line?

Students can enter an individual Python code line and receive an explanation of:

- What the line does
- Why it is needed
- A question that encourages understanding

### 5. Guided Code Construction

The system can guide students through solution construction step-by-step instead of generating the complete program immediately.

### 6. Final Solution Generation

After the reasoning and construction stages, the system can provide a complete Python solution with an explanation.

---

## System Architecture

```text
                    Student
                       |
                       v
               Streamlit Web UI
                       |
                       v
                  Flask API
                       |
              +--------+--------+
              |                 |
              v                 v
        RAG Retrieval       Local LLM
              |                 |
              v                 v
            FAISS          Qwen2.5-1.5B
              |                 |
              +--------+--------+
                       |
                       v
              Teaching Response
                       |
                       v
        Hints / Explanation / Solution
