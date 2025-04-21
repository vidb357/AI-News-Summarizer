import streamlit as st

def load_css():
    css = """
    /* Enhanced search button styling */
    .search-button > div > button {
        background-color: #32CD32 !important;
        color: white !important;
        border: none !important;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }

    .search-button > div > button:hover {
        background-color: #2BB62B !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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

    /* Additional interface improvements */
    .news-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        border: 1px solid #f0f0f0;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .news-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
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
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


