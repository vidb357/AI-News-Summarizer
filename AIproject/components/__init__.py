# This file needs to be created in each directory to make it a Python package:
# - utils/__init__.py
# - services/__init__.py
# - components/__init__.py

# For each directory, create an empty __init__.py file or add imports if needed
# Example for utils/__init__.py:
from utils.date_utils import format_date

# Example for services/__init__.py:
from services.news_service import fetch_news
from services.ai_service import load_models, summarize_article, generate_headline, analyze_sentiment

# Example for components/__init__.py:
from components.sidebar import render_sidebar
from components.news_card import display_news_cards