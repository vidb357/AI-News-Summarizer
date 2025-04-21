import streamlit as st
from services.recommendation_service import get_personalized_news, filter_articles_by_topic
from services.user_preferences import initialize_preferences, add_favorite_topic, remove_favorite_topic
from components.news_card import display_news_cards
from utils.ui_utils import display_error_message, display_success_message
import time

def render_recommendations_page(news_api_key, summary_model, headline_model, sentiment_model):
    """Render the personalized recommendations page"""
    st.markdown("<h1 class='main-header'>Your Personalized News</h1>", unsafe_allow_html=True)
    st.markdown(
        "Discover news tailored to your interests and reading history."
    )
    
    # Initialize user preferences
    initialize_preferences()
    
    # Create tabs - removed the Preferences tab
    tab1, tab2 = st.tabs(["For You", "Reading History"])
    
    # Tab 1: For You (Recommendations)
    with tab1:
        if news_api_key:
            with st.spinner("Fetching personalized news..."):
                recommended_articles, topics_used = get_personalized_news(
                    news_api_key, count=6, sort_by="relevancy"
                )
                
                # Simulate loading time for better UX
                time.sleep(0.5)
            
            if recommended_articles:
                st.success(f"Here are news articles based on your interests: {', '.join(topics_used)}")
                
                # Display recommended articles
                display_news_cards(recommended_articles, summary_model, headline_model, sentiment_model)
                
                # Add interaction options
                with st.expander("Customize your recommendations"):
                    topic_col1, topic_col2 = st.columns(2)
                    
                    with topic_col1:
                        new_topic = st.text_input("Add a topic you're interested in:")
                        if st.button("Add to Interests", key="add_interest"):
                            if new_topic:
                                add_favorite_topic(new_topic)
                                st.success(f"Added '{new_topic}' to your interests!")
                                st.experimental_rerun()
                    
                    with topic_col2:
                        if st.session_state.user_preferences['favorite_topics']:
                            topic_to_remove = st.selectbox(
                                "Select a topic to remove from interests:", 
                                options=st.session_state.user_preferences['favorite_topics']
                            )
                            if st.button("Remove Interest", key="remove_interest"):
                                remove_favorite_topic(topic_to_remove)
                                st.success(f"Removed '{topic_to_remove}' from your interests!")
                                st.experimental_rerun()
            else:
                st.warning("No personalized articles found. Try adding some interests using the customization options.")
        else:
            display_error_message("Please set your NewsAPI key in the sidebar to get personalized recommendations.")
                    
    # Tab 2: Reading History
    with tab2:
        st.markdown("### Your Reading History")
        
        if st.session_state.user_preferences['reading_history']:
            for i, article in enumerate(st.session_state.user_preferences['reading_history']):
                with st.container():
                    st.markdown(f"**{i+1}. [{article['title']}]({article['url']})**")
                    st.markdown(f"Source: {article['source']} • Read on: {article['timestamp']}")
                    st.markdown("---")
        else:
            st.write("Your reading history is empty. Articles you read will appear here.")