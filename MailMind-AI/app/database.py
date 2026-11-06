import sqlite3
from pathlib import Path
from app.config import settings

def connect():
    Path(settings.database_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(settings.database_path)
    conn.execute('CREATE TABLE IF NOT EXISTS processed_messages (message_id TEXT PRIMARY KEY, category TEXT NOT NULL, processed_at TEXT DEFAULT CURRENT_TIMESTAMP)')
    return conn

def is_processed(message_id: str) -> bool:
    with connect() as conn:
        return conn.execute('SELECT 1 FROM processed_messages WHERE message_id = ?', (message_id,)).fetchone() is not None

def mark_processed(message_id: str, category: str):
    with connect() as conn:
        conn.execute('INSERT OR IGNORE INTO processed_messages(message_id, category) VALUES (?, ?)', (message_id, category))
