from services.news_service import fetch_news
from services.ai_service import load_models, summarize_article, generate_headline, analyze_sentiment
from services.user_preferences import (
    initialize_preferences,
    add_to_reading_history,
    add_favorite_topic,
    remove_favorite_topic,
    add_excluded_topic,
    add_preferred_source,
    add_blocked_source,
    get_recommended_topics,
    export_preferences,
    import_preferences
)
from services.recommendation_service import get_personalized_news, filter_articles_by_topic