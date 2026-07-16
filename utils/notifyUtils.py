import requests
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

TELEGRAM_MESSAGE_LIMIT = 4096

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


def chunk_message(
    text: str,
    limit: int = TELEGRAM_MESSAGE_LIMIT,
) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=limit,
        chunk_overlap=0,
        separators=["\n\n", "\n", " "]
    )
    return text_splitter.split_text(text)


def send_telegram_message(
    bot_token: str,
    chat_id: str,
    path: str = "digest.md",
) -> None:
    message = load_digest(path)
    for chunk in chunk_message(message):
        response = requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": chunk,
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
