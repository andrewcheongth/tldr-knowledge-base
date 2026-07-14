import requests
from pathlib import Path

def load_digest(path: str = "digest.md") -> str:
    digest_path = Path(path)
    if not digest_path.exists():
        raise FileNotFoundError(
            f"{path} not found — the digest pipeline may have failed upstream"
        )
    content = digest_path.read_text().strip()
    if not content:
        raise ValueError(f"{path} exists but is empty")
    return content

def send_telegram_message(
    bot_token: str,
    chat_id: str,
    path: str = "digest.md",
) -> None:
    message = load_digest(path)
    response = requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
            "disable_web_page_preview": False,
        },
        timeout=10,
    )
    response.raise_for_status()


if __name__ == "__main__":
    import os
    send_telegram_message(
        bot_token=os.environ["TELEGRAM_BOT_TOKEN"],
        chat_id=os.environ["TELEGRAM_CHAT_ID"],
    )
