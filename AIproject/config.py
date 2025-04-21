import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="AI News Summarizer Pro",
        page_icon="📰",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def load_css():
    css = """
    /* Enhanced search button styling - now orange */
    .search-button > div > button {
        background-color: #FF8C00 !important;
        color: white !important;
        border: none !important;
        font-weight: 600;
        transition: background-color 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    .search-button > div > button:hover {
        background-color: #FF7000 !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Fix vertical alignment for search bar and button */
    div.row-widget.stButton {
        margin-top: 0;
        margin-bottom: 0;
        padding-top: 0;
        padding-bottom: 0;
    }
    
    div.row-widget.stTextInput {
        margin-bottom: 0;
        padding-bottom: 0;
    }
    
    /* Center alignment fixes */
    [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    
    /* Improved card interface */
    .news-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
        margin-bottom: 2rem;
        border: 1px solid #f0f0f0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .news-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
    }
    
    /* Improved links styling */
    a {
        color: #1E88E5;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    
    a:hover {
        color: #1565C0;
        text-decoration: underline;
    }
    
    /* Better summary visibility */
    .ai-summary {
        background-color: #f8f9fa;
        padding: 1.25rem;
        border-radius: 8px;
        border-left: 4px solid #3949AB;
        margin: 1rem 0;
        line-height: 1.6;
        font-size: 1.05rem;
    }
    
    /* Header for summary section */
    .summary-header {
        font-weight: 600;
        color: #3949AB;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)