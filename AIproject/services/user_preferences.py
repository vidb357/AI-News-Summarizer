import streamlit as st
from datetime import datetime
import json

def initialize_preferences():
    """Initialize user preferences in session state if not already present"""
    if 'user_preferences' not in st.session_state:
        st.session_state.user_preferences = {
            'favorite_topics': [],
            'excluded_topics': [],
            'preferred_sources': [],
            'blocked_sources': [],
            'reading_history': [],
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

def add_to_reading_history(article):
    """Add an article to the user's reading history"""
    initialize_preferences()
    
    # Extract relevant information from the article
    article_data = {
        'title': article.get('title', ''),
        'url': article.get('url', ''),
        'source': article.get('source', {}).get('name', 'Unknown'),
        'publishedAt': article.get('publishedAt', ''),
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Add to reading history, avoid duplicates based on URL
    history = st.session_state.user_preferences['reading_history']
    if not any(item['url'] == article_data['url'] for item in history):
        history.insert(0, article_data)  # Add at the beginning
        # Keep only the last 50 articles
        st.session_state.user_preferences['reading_history'] = history[:50]

def add_favorite_topic(topic):
    """Add a topic to user's favorite topics"""
    initialize_preferences()
    if topic and topic not in st.session_state.user_preferences['favorite_topics']:
        st.session_state.user_preferences['favorite_topics'].append(topic)
        # Remove from excluded if it was there
        if topic in st.session_state.user_preferences['excluded_topics']:
            st.session_state.user_preferences['excluded_topics'].remove(topic)

def remove_favorite_topic(topic):
    """Remove a topic from user's favorite topics"""
    initialize_preferences()
    if topic in st.session_state.user_preferences['favorite_topics']:
        st.session_state.user_preferences['favorite_topics'].remove(topic)

def add_excluded_topic(topic):
    """Add a topic to user's excluded topics"""
    initialize_preferences()
    if topic and topic not in st.session_state.user_preferences['excluded_topics']:
        st.session_state.user_preferences['excluded_topics'].append(topic)
        # Remove from favorites if it was there
        if topic in st.session_state.user_preferences['favorite_topics']:
            st.session_state.user_preferences['favorite_topics'].remove(topic)

def add_preferred_source(source):
    """Add a source to user's preferred sources"""
    initialize_preferences()
    if source and source not in st.session_state.user_preferences['preferred_sources']:
        st.session_state.user_preferences['preferred_sources'].append(source)
        # Remove from blocked if it was there
        if source in st.session_state.user_preferences['blocked_sources']:
            st.session_state.user_preferences['blocked_sources'].remove(source)

def add_blocked_source(source):
    """Add a source to user's blocked sources"""
    initialize_preferences()
    if source and source not in st.session_state.user_preferences['blocked_sources']:
        st.session_state.user_preferences['blocked_sources'].append(source)
        # Remove from preferred if it was there
        if source in st.session_state.user_preferences['preferred_sources']:
            st.session_state.user_preferences['preferred_sources'].remove(source)

def get_recommended_topics():
    """Get recommended topics based on user's reading history and preferences"""
    initialize_preferences()
    
    # Start with favorite topics
    recommended = set(st.session_state.user_preferences['favorite_topics'])
    
    # Add topics from reading history
    if st.session_state.user_preferences['reading_history']:
        # This is a simplified approach - in a real app you might use NLP to extract topics
        for article in st.session_state.user_preferences['reading_history'][:10]:  # Last 10 read articles
            # Extract potential topics from the title
            title = article['title'].lower()
            # Simple example - in a real app you'd use entity extraction or topic modeling
            potential_topics = [
                word.capitalize() for word in title.split() 
                if len(word) > 4 and word not in ['about', 'after', 'again', 'their', 'there', 'would', 'could']
            ]
            recommended.update(potential_topics)
    
    # Remove excluded topics
    recommended = recommended - set(st.session_state.user_preferences['excluded_topics'])
    
    # Return as list, limit to 10 topics
    return list(recommended)[:10]

def export_preferences():
    """Export user preferences as JSON string"""
    initialize_preferences()
    return json.dumps(st.session_state.user_preferences, indent=2)

def import_preferences(json_data):
    """Import user preferences from JSON string"""
    try:
        st.session_state.user_preferences = json.loads(json_data)
        st.session_state.user_preferences['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return True
    except Exception as e:
        st.error(f"Error importing preferences: {e}")
        return False