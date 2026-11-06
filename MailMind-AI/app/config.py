import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    gmail_credentials_file: str = os.getenv('GMAIL_CREDENTIALS_FILE', 'credentials.json')
    gmail_token_file: str = os.getenv('GMAIL_TOKEN_FILE', 'token.json')
    gmail_query: str = os.getenv('GMAIL_QUERY', 'newer_than:2d')
    poll_interval_minutes: int = int(os.getenv('POLL_INTERVAL_MINUTES', '10'))
    database_path: str = os.getenv('DATABASE_PATH', 'data/mailmind.sqlite3')
    telegram_bot_token: str = os.getenv('TELEGRAM_BOT_TOKEN', '')
    telegram_chat_id: str = os.getenv('TELEGRAM_CHAT_ID', '')
    ai_provider: str = os.getenv('AI_PROVIDER', 'none').lower()
    gemini_api_key: str = os.getenv('GEMINI_API_KEY', '')
    gemini_model: str = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash')
    openai_api_key: str = os.getenv('OPENAI_API_KEY', '')
    openai_model: str = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
    playwright_headless: bool = os.getenv('PLAYWRIGHT_HEADLESS', 'true').lower() == 'true'

settings = Settings()
