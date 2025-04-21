import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_models():
    """Load and cache AI models"""
    summary_model = pipeline("summarization")
    headline_model = pipeline("summarization", model="google/pegasus-xsum")
    sentiment_model = pipeline("sentiment-analysis")
    return summary_model, headline_model, sentiment_model

def summarize_article(content, model):
    """Generate a summary for news article content"""
    try:
        if content:
            content = content[:1024]  # Limit content length
            summary = model(content, max_length=150, min_length=50, do_sample=False)
            return summary[0]['summary_text']
        else:
            return "No content available to summarize."
    except Exception as e:
        return f"Error summarizing: {e}"

def generate_headline(content, model):
    """Generate a catchy headline for news article content"""
    try:
        if content:
            content = content[:512]  # Limit content length
            headline = model(
                content,
                max_length=25,
                min_length=10,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                clean_up_tokenization_spaces=True
            )
            return headline[0]['summary_text'].strip().capitalize()
        else:
            return "No headline available."
    except Exception as e:
        return f"Error generating headline: {e}"

def analyze_sentiment(content, model):
    """Analyze sentiment of news article content"""
    try:
        if content:
            # Limit content for sentiment analysis
            content = content[:512]
            result = model(content)[0]
            return {
                "label": result["label"], 
                "score": round(result["score"] * 100, 1)
            }
        else:
            return {"label": "NEUTRAL", "score": 0}
    except Exception as e:
        return {"label": "NEUTRAL", "score": 0}