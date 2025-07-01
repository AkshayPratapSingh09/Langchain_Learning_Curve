import streamlit as st
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

# UI Setup
st.title("📚 Research Paper Summarizer using Gemini")

# Sample top 5 papers (mock)
papers = {
    "Transformers Are All You Need": "A foundational paper introducing Transformer models.",
    "Attention Is All You Need": "The original paper defining the Transformer architecture.",
    "BERT: Pre-training of Deep Bidirectional Transformers": "Introduced BERT, bidirectional pretraining technique.",
    "GPT-3: Language Models are Few-Shot Learners": "Presents GPT-3 and few-shot learning.",
    "PaLM 2: Scaling Language Models with Pathways": "Google’s research into large model training and scaling."
}

explanation_styles = ["Layman-friendly", "Technical Summary", "Academic Reviewer Style", "Bullet Points", "Analogy-based"]
summary_lengths = ["Short (50-100 words)", "Medium (100-200 words)", "Long (200+ words)"]

# Dropdowns
selected_paper = st.selectbox("📄 Choose a Research Paper", list(papers.keys()))
selected_style = st.selectbox("🧠 Explanation Style", explanation_styles)
selected_length = st.selectbox("📏 Summary Length", summary_lengths)

# Button
if st.button("✨ Summarize"):
    with st.spinner("Generating summary..."):

        # Dynamic prompt construction
        template = ChatPromptTemplate("""
        You are a helpful AI trained in summarizing research papers. 
        Provide a summary of the following paper in the style of "{style}" and the length category "{length}".

        Paper Title: "{title}"
        Abstract: "{abstract}"

        Ensure the summary is coherent, informative, and well-written.
        """)

        prompt = prompt_template.format_messages(
            style=selected_style,
            length=selected_length,
            title=selected_paper,
            abstract=papers[selected_paper]
        )

        result = llm.invoke(prompt)
        st.markdown("### 🔍 Generated Summary")
        st.success(result.content)
