import streamlit as st
import requests

def fetch_news(api_key, topic, page_size=5, sort_by="publishedAt"):
    """Fetch news articles from NewsAPI based on topic and parameters"""
    try:
        url = (f"https://newsapi.org/v2/everything?q={topic}&language=en"
               f"&pageSize={page_size}&sortBy={sort_by}&apiKey={api_key}")
        response = requests.get(url)
        data = response.json()
        if data.get('status') == 'error':
            st.error(f"API Error: {data.get('message')}")
            return []
        return data.get('articles', [])
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return []