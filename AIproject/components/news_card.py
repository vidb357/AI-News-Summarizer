import streamlit as st
import time
from datetime import datetime

def display_news_cards(articles, summary_model, headline_model, sentiment_model):
    """Display news articles as cards with AI-enhanced content"""
    
    if not articles:
        st.warning("No articles to display.")
        return
    
    for article in articles:
        with st.container():
            # Card container
            st.markdown("<div class='news-card'>", unsafe_allow_html=True)
            
            # Title
            st.markdown(f"<h2 class='news-headline'>{article.get('title', 'No title available')}</h2>", 
                       unsafe_allow_html=True)
            
            # Metadata (source, date)
            st.markdown(f"<div class='news-metadata'>{article.get('source', {}).get('name', 'Unknown source')} • "
                       f"{format_date(article.get('publishedAt', ''))}</div>", 
                       unsafe_allow_html=True)
            
            # Display image if available - FIX: remove use_column_width
            if article.get('urlToImage'):
                st.image(article.get('urlToImage'))
            
            # Generate sentiment analysis
            sentiment = analyze_sentiment(article.get('description', ''), sentiment_model)
            
            # Display sentiment analysis
            st.markdown("<strong>Sentiment Analysis:</strong>", unsafe_allow_html=True)
            st.markdown(render_sentiment_badge(sentiment), unsafe_allow_html=True)
            
            # AI Summary - make it explicitly visible
            st.markdown("<div class='summary-header'>AI Summary:</div>", unsafe_allow_html=True)
            
            # Get summary text
            summary_text = generate_summary(article, summary_model)
            
            # Display summary text in a highlighted box
            st.markdown(f"<div class='summary-text'>{summary_text}</div>", unsafe_allow_html=True)
            
            # Original title
            st.markdown("<strong>Original Title:</strong>", unsafe_allow_html=True)
            st.markdown(generate_alternative_headline(article, headline_model))
            
            # Read more link
            st.markdown(f"<a href='{article.get('url', '#')}' target='_blank'>Read full article →</a>", 
                      unsafe_allow_html=True)
            
            # Close card container
            st.markdown("</div>", unsafe_allow_html=True)

def format_date(date_str):
    """Format date string to a readable format"""
    if not date_str:
        return "Unknown date"
    
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%B %d, %Y • %I:%M %p")
    except:
        return date_str

def generate_summary(article, model):
    """Generate AI summary of the article"""
    # In a real app, this would use the AI model
    # For demonstration, create a more visible summary
    content = article.get('description', article.get('content', 'No content available'))
    if not content or content == 'No content available':
        content = "This article discusses advancements in technology. The AI model would typically generate a comprehensive summary here based on the full article content."
    return content

def generate_alternative_headline(article, model):
    """Generate an alternative headline for the article"""
    # In a real app, this would use the AI model
    return article.get('title', 'No title available')

def analyze_sentiment(text, model):
    """Analyze sentiment of the article"""
    # In a real implementation, this would use the sentiment model
    # For now, return a simple mock result
    import random
    labels = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    selected = random.choice(labels)
    score = random.randint(65, 98)
    
    return {
        "label": selected,
        "score": score
    }

def render_sentiment_badge(sentiment):
    """Render a sentiment badge with appropriate styling"""
    sentiment_class = f"sentiment-{sentiment['label'].lower()}"
    sentiment_icon = {"POSITIVE": "😊", "NEGATIVE": "😞", "NEUTRAL": "😐"}.get(sentiment['label'], "")
    
    return (
        f"<span class='sentiment-badge {sentiment_class}'>{sentiment_icon} "
        f"{sentiment['label']} ({sentiment['score']}%)</span>"
    )