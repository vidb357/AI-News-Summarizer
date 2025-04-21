# AI-News-Summarizer


## 📰 AI News Summarizer Pro

**AI News Summarizer Pro** is an advanced, AI-powered web application built with **Streamlit** that brings you the latest news in a concise, personalized, and user-friendly format. It uses **NLP models** to generate summaries, headlines, and sentiment analysis of news articles across a wide range of topics.

### ✨ Key Features

- 🔍 **Search & Summarize:** Enter any topic and instantly fetch the latest news articles with AI-generated summaries and headlines.
- 📚 **Popular Topics:** Quickly browse news from trending categories like Technology, Health, Business, Politics, Sports, and Entertainment.
- 💡 **Sentiment Analysis:** Understand the emotional tone behind the news using AI-powered sentiment scoring.
- 🧠 **Personalized Feed:** A "For You" section that shows recommendations based on your reading history and preferences.
- 🎨 **Sleek UI:** A fully responsive and elegant interface styled with custom CSS to deliver an intuitive reading experience.

### ⚙️ Tech Stack

- **Frontend & Framework:** Streamlit
- **Backend Services:** NewsAPI.org
- **AI Models:** Transformers / Hugging Face (or any custom NLP models)
- **Styling:** Custom CSS with enhanced layout and interaction design

### 📦 Project Structure

```
├── app.py                       # Main Streamlit app
├── config.py                   # Page config & CSS loader
├── styles.py                   # Custom CSS styles as a string
├── components/
│   ├── sidebar.py              # Sidebar with user settings
│   ├── news_card.py            # Renders news cards
│   └── recommendations_page.py # Personalized "For You" section
├── services/
│   ├── news_service.py         # Handles API calls to NewsAPI
│   ├── ai_service.py           # Loads NLP models
│   └── user_preferences.py     # Manages reading history/preferences
└── utils/
    └── ui_utils.py             # UI helper functions for messages/buttons
```

### 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/ai-news-summarizer.git
   cd ai-news-summarizer
   ```

2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

3. Set your [NewsAPI](https://newsapi.org/) key in the sidebar or a `.env` file.

4. Run the app  
   ```bash
   streamlit run app.py
   ```

