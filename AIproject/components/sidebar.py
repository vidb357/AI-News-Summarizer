import streamlit as st

def render_sidebar():
    """Render the sidebar and return user settings"""
    with st.sidebar:
        st.image("https://via.placeholder.com/150x100?text=NewsAI", width=150)
        st.markdown("<h2 class='main-header'>Settings</h2>", unsafe_allow_html=True)
        
        # API Key input (with masking)
        news_api_key = st.text_input(
            "NewsAPI Key",
            value="e637634d2c2748a49779c467c4baa807",
            type="password",
            help="Enter your NewsAPI key here"
        )
        
        # Advanced settings
        st.markdown("### Advanced Settings")
        news_count = st.slider("Number of articles", min_value=1, max_value=10, value=5)
        sort_option = st.selectbox(
            "Sort articles by",
            options=["publishedAt", "relevancy", "popularity"],
            index=0
        )
        
        # About section
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
        **AI News Summarizer Pro** uses advanced natural language processing to:
        - Find latest news on any topic
        - Generate concise summaries
        - Create catchy headlines
        - Analyze emotional tone
        - Provide personalized recommendations
        """)
        st.markdown("---")
        st.markdown("© 2025 NewsAI Pro")
    
    return news_api_key, news_count, sort_option