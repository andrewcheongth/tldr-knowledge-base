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
    timestamp = int(today_date.timestamp())
    response = requests.get(
        f"https://hn.algolia.com/api/v1/search_by_date",
        params={
            "tags": "story",
            "numericFilters": f"created_at_i>{timestamp}",
            "hitsPerPage": 500
        },
        timeout=10
    )
    return response.json().get("hits", [])


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