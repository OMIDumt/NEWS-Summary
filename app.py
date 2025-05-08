import streamlit as st
from transformers import pipeline

# Load summarization pipeline (cached on first run)
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# App title
st.title("📰 News Article Summarizer")
st.write("Paste a long news article below and get a short, bullet-point summary.")

# Text input
article_text = st.text_area("Enter your news article here:", height=300)

# Generate summary
if st.button("Summarize"):
    if article_text.strip() == "":
        st.warning("Please paste an article before clicking summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(article_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        
        st.subheader("🔍 Summary")
        # Optional: Format summary into bullet points
        bullets = summary.split(". ")
        for bullet in bullets:
            if bullet.strip():
                st.markdown(f"- {bullet.strip()}.")

