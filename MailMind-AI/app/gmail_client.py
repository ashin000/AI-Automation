import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from app.config import settings

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    creds = None
    try:
        creds = Credentials.from_authorized_user_file(settings.gmail_token_file, SCOPES)
    except (FileNotFoundError, ValueError):
        pass
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(settings.gmail_credentials_file, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(settings.gmail_token_file, 'w', encoding='utf-8') as file:
            file.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds, cache_discovery=False)

def _decode(data: str) -> str:
    return base64.urlsafe_b64decode(data + '=' * (-len(data) % 4)).decode('utf-8', errors='replace')

def _body(payload: dict) -> str:
    mime = payload.get('mimeType', '')
    data = payload.get('body', {}).get('data')
    if data and mime == 'text/plain':
        return _decode(data)
    if data and mime == 'text/html':
        from bs4 import BeautifulSoup
        return BeautifulSoup(_decode(data), 'html.parser').get_text(' ', strip=True)
    parts = payload.get('parts', []) or []
    return '\n'.join(filter(None, (_body(part) for part in parts)))

def fetch_messages(service, query: str, limit: int = 30):
    listing = service.users().messages().list(userId='me', q=query, maxResults=limit).execute()
    output = []
    for item in listing.get('messages', []):
        raw = service.users().messages().get(userId='me', id=item['id'], format='full').execute()
        headers = {h['name'].lower(): h['value'] for h in raw.get('payload', {}).get('headers', [])}
        output.append({'id': raw['id'], 'from': headers.get('from', ''), 'subject': headers.get('subject', '(No subject)'), 'date': headers.get('date', ''), 'body': _body(raw.get('payload', {}))[:12000], 'snippet': raw.get('snippet', '')})
    return output
