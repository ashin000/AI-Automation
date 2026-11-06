from app.config import settings
from app.gmail_client import authenticate, fetch_messages
from app.classifier import classify_email
from app.summarizer import summarize
from app.telegram_bot import send_message
from app.database import is_processed, mark_processed


def run_agent():
    service = authenticate()
    emails = fetch_messages(service, settings.gmail_query)
    notified = 0
    for email in emails:
        if is_processed(email['id']):
            continue
        result = classify_email(email)
        if result.category not in {'BANK_ALERT', 'SECURITY_ALERT', 'TLDR_NEWSLETTER'}:
            mark_processed(email['id'], result.category)
            continue
        summary = summarize(email, result.category)
        icon = '🚨' if result.category == 'SECURITY_ALERT' else '🏦' if result.category == 'BANK_ALERT' else '📰'
        message = (f'{icon} {result.category.replace("_", " ")}\nPriority: {result.priority}\n'
                   f'From: {email["from"][:160]}\nSubject: {email["subject"][:200]}\n\n'
                   f'{summary}\n\nMailMind AI')
        send_message(message)
        mark_processed(email['id'], result.category)
        notified += 1
    return {'checked': len(emails), 'notified': notified}
