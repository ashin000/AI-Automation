import requests
from app.config import settings

def send_message(text: str) -> bool:
    if not settings.telegram_bot_token or not settings.telegram_chat_id:
        print('[Telegram not configured]\n' + text)
        return False
    response = requests.post(f'https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage', json={'chat_id': settings.telegram_chat_id, 'text': text[:4000], 'disable_web_page_preview': True}, timeout=20)
    response.raise_for_status()
    return True
