import streamlit as st
from config import set_page_config, load_css
from components.sidebar import render_sidebar
from components.news_card import display_news_cards
from components.recommendations_page import render_recommendations_page
from services.news_service import fetch_news
from services.ai_service import load_models
from services.user_preferences import add_to_reading_history, initialize_preferences
from utils.ui_utils import (
    display_error_message, display_success_message, 
    display_warning_message, render_topic_buttons,
    load_ui_styles
)
import time

def main():
    # Set page configuration and load CSS
    set_page_config()
    load_css()
    load_ui_styles()  # Load the additional UI styles from ui_utils
    
    # Initialize user preferences
    initialize_preferences()
    
    # Render sidebar and get user settings
    news_api_key, news_count, sort_option = render_sidebar()
    
    # Create navigation tabs
    tab1, tab2 = st.tabs(["News Search", "For You"])
    
    # Load AI models - load once for both tabs
    summary_model, headline_model, sentiment_model = load_models()
    
    # Tab 1: News Search (Original functionality)
    with tab1:
        st.markdown("<h1 class='main-header'>AI News Summarizer Pro</h1>", unsafe_allow_html=True)
        st.markdown(
            "Get AI-powered summaries, headlines, and sentiment analysis for the latest news on any topic."
        )
        
        # Topic selection
        st.markdown("<h3>Popular Topics</h3>", unsafe_allow_html=True)
        
        # Initialize topic in session state if not already set
        if 'topic' not in st.session_state:
            st.session_state.topic = "Technology"
        
        # Create topic buttons using utility function
        cols = st.columns(6)
        topics = ["Technology", "Health", "Business", "Politics", "Sports", "Entertainment"]
        selected_topic = render_topic_buttons(topics, cols)
        
        if selected_topic:
            st.session_state.topic = selected_topic
        
        # Custom topic search
        st.markdown("<h3>Custom Search</h3>", unsafe_allow_html=True)
        
        # Better aligned search bar and button using columns
        search_col1, search_col2 = st.columns([4, 1])
        
        with search_col1:
            topic = st.text_input(
                "Enter a topic to search for:",
                value=st.session_state.topic,
                key="topic_input",
                label_visibility="collapsed"
            )
        
        with search_col2:
            # Apply orange search button styling
            st.markdown('<div class="search-button">', unsafe_allow_html=True)
            search_clicked = st.button(
                "Search News",
                key="search_button",
                use_container_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Display loading spinner and results
        if search_clicked or 'last_search' in st.session_state:
            if search_clicked:
                st.session_state.last_search = topic
            
            topic = st.session_state.last_search
            
            if not news_api_key:
                display_error_message("Please set your NewsAPI key in the sidebar.")
            else:
                # Show progress
                with st.spinner(f"Searching for latest news on '{topic}'..."):
                    articles = fetch_news(news_api_key, topic, news_count, sort_option)
                    
                    # Simulate loading time for better UX
                    time.sleep(0.5)
                
                # Show results
                if not articles:
                    display_warning_message(f"No articles found for '{topic}'. Try another search term.")
                else:
                    display_success_message(f"Found {len(articles)} articles about '{topic}'")
                    
                    # Update reading history when showing articles
                    for article in articles:
                        add_to_reading_history(article)
                    
                    # Display news cards
                    display_news_cards(articles, summary_model, headline_model, sentiment_model)
    
    # Tab 2: For You (Personalized recommendations)
    with tab2:
        render_recommendations_page(news_api_key, summary_model, headline_model, sentiment_model)

if __name__ == "__main__":
    main()