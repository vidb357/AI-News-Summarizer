import streamlit as st
from services.news_service import fetch_news
from services.user_preferences import get_recommended_topics, initialize_preferences
import random

def get_personalized_news(api_key, count=5, sort_by="publishedAt"):
    """Get personalized news based on user preferences"""
    initialize_preferences()
    
    # Get recommended topics
    topics = get_recommended_topics()
    
    # If no recommended topics, use some general ones
    if not topics:
        topics = ["Technology", "Science", "Health", "Business"]
    
    # Choose 2-3 random topics from the list to diversify results
    if len(topics) > 3:
        query_topics = random.sample(topics, k=min(3, len(topics)))
    else:
        query_topics = topics
    
    # Combine topics into a query
    query = " OR ".join(query_topics)
    
    # Get news articles
    articles = fetch_news(api_key, query, count, sort_by)
    
    # Filter out blocked sources if any
    if st.session_state.user_preferences['blocked_sources']:
        articles = [
            article for article in articles 
            if article.get('source', {}).get('name') not in st.session_state.user_preferences['blocked_sources']
        ]
    
    # Prioritize preferred sources if any
    if st.session_state.user_preferences['preferred_sources']:
        # Move preferred sources to the top
        preferred = [
            article for article in articles 
            if article.get('source', {}).get('name') in st.session_state.user_preferences['preferred_sources']
        ]
        others = [
            article for article in articles 
            if article.get('source', {}).get('name') not in st.session_state.user_preferences['preferred_sources']
        ]
        articles = preferred + others
    
    return articles, query_topics

def filter_articles_by_topic(articles, topic):
    """Filter articles by a specific topic"""
    # This is a simple keyword-based filter - a real implementation would use NLP
    filtered = []
    topic_lower = topic.lower()
    
    for article in articles:
        title = article.get('title', '').lower()
        description = article.get('description', '').lower()
        content = article.get('content', '').lower()
        
        if (topic_lower in title or 
            topic_lower in description or 
            topic_lower in content):
            filtered.append(article)
    
    return filtered