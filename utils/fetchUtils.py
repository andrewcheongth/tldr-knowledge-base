import requests, time, trafilatura
from datetime import datetime, timedelta


def fetch_hackernews(today_date: datetime) -> list[dict]:
    """
    Fetches the latest articles from Hacker News that were published today.
    
    Args:
        today_date (datetime): The date to filter articles by.
        
    Returns:
        list[dict]: A list of article metadata in dictionary format published today.
    """
    ids = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json").json()
    articles = []
    for id in ids:
        article = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json").json()
        if article.get("type") != "story":
            continue
        published_time = datetime.fromtimestamp(article.get("time"))
        if published_time >= today_date:
            articles.append(article)
    return articles


def fetch_article_content(url: str) -> str:
    """
    Fetches the content of an article from a given URL using trafilatura.
    
    Args:
        url (str): The URL of the article to fetch.
        
    Returns:
        str: The extracted content of the article.
    """
    response = trafilatura.fetch_url(url)
    if response is None:
        return ""
    return trafilatura.extract(response)