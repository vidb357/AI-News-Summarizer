import streamlit as st

def display_error_message(message):
    """Display styled error message"""
    st.error(f"🚫 {message}")

def display_success_message(message):
    """Display styled success message"""
    st.success(f" {message}")

def display_warning_message(message):
    """Display styled warning message"""
    st.warning(f"⚠️ {message}")

def display_info_message(message):
    """Display styled info message"""
    st.info(f"ℹ️ {message}")

def create_placeholder_image_url(width=300, height=200, text="No+Image"):
    """Create a URL for a placeholder image"""
    return f"https://via.placeholder.com/{width}x{height}?text={text}"

def render_sentiment_badge(sentiment):
    """Render a sentiment badge with appropriate styling"""
    sentiment_class = f"sentiment-{sentiment['label'].lower()}"
    sentiment_icon = {"POSITIVE": "😊", "NEGATIVE": "😞", "NEUTRAL": "😐"}.get(sentiment['label'], "")
    
    return (
        f"<span class='sentiment-badge {sentiment_class}'>{sentiment_icon} "
        f"{sentiment['label']} ({sentiment['score']}%)</span>"
    )

def render_topic_buttons(topics, columns=None):
    """Render topic selection buttons in columns"""
    if columns is None:
        columns = st.columns(len(topics))
    
    selected_topic = None
    
    for i, topic in enumerate(topics):
        with columns[i]:
            if st.button(topic, key=f"btn_{topic}", use_container_width=True):
                selected_topic = topic
    
    return selected_topic

# Function to load CSS styles
def load_ui_styles():
    """Load all UI CSS styles"""
    st.markdown(CSS_STYLES, unsafe_allow_html=True)

# Enhanced CSS with more modern and polished styling
CSS_STYLES = """
<style>
/* Main app styling */
.main-header {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: #1E3A8A;
    font-weight: 700;
    margin-bottom: 1rem;
}

/* Search button styling - Orange */
.search-button button {
    background-color: #FF8C00 !important;
    color: white !important;
    border: none !important;
    font-weight: 600;
    transition: background-color 0.3s ease;
}

.search-button button:hover {
    background-color: #FF7000 !important;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* News card styling */
.news-card {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
    margin-bottom: 2rem;
    border: 1px solid #f0f0f0;
}

.news-headline {
    color: #1E3A8A;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 0.75rem;
    line-height: 1.3;
    font-size: 1.4rem;
}

.news-metadata {
    color: #6c757d;
    font-size: 0.85rem;
    margin-bottom: 1rem;
}

/* Make summary extremely visible */
.summary-text {
    background-color: #EFF6FF !important;
    border-left: 5px solid #3B82F6 !important;
    padding: 15px !important;
    margin: 15px 0 !important;
    font-size: 1.05rem !important;
    line-height: 1.6 !important;
    color: #1E293B !important;
    border-radius: 6px !important;
    display: block !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
}

.summary-header {
    font-weight: 600;
    color: #2563EB;
    margin-top: 15px;
    margin-bottom: 5px;
    font-size: 1.1rem;
    display: block;
}

/* Sentiment badges styling */
.sentiment-badge {
    padding: 5px 10px;
    border-radius: 16px;
    font-weight: 500;
    display: inline-block;
    font-size: 0.85rem;
    margin: 10px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.sentiment-positive {
    background-color: rgba(76, 175, 80, 0.15);
    color: #2e7d32;
    border: 1px solid rgba(76, 175, 80, 0.3);
}

.sentiment-negative {
    background-color: rgba(244, 67, 54, 0.15);
    color: #c62828;
    border: 1px solid rgba(244, 67, 54, 0.3);
}

.sentiment-neutral {
    background-color: rgba(158, 158, 158, 0.15);
    color: #616161;
    border: 1px solid rgba(158, 158, 158, 0.3);
}

/* Links styling */
a {
    color: #2563EB;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s ease;
    margin-top: 10px;
    display: inline-block;
}

a:hover {
    color: #1D4ED8;
    text-decoration: underline;
}

/* Header and sections styling */
h3 {
    color: #333;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
    font-weight: 600;
}
</style>
"""