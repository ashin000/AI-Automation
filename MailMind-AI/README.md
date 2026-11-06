# MailMind AI

AI-powered email intelligence that classifies important Gmail messages and sends concise summaries to Telegram.

## Features

- Gmail OAuth 2.0 integration using read-only access.
- Playwright browser automation helper for authorized browser workflows.
- Rule-assisted classification for bank alerts, security alerts, TLDR newsletters, and other mail.
- Optional Gemini or OpenAI summaries, with a local fallback.
- Telegram notifications for important messages.
- SQLite deduplication so a message is notified only once.
- Scheduled polling and manual one-shot runs.
- Redaction of common sensitive values before notification.

## Architecture

Gmail API is the reliable mailbox ingestion path. Playwright is included for browser automation tasks; it does not store Gmail passwords or bypass OAuth. This gives the project both dependable email access and hands-on browser automation.

## Setup

1. Use Python 3.11+.
2. In Google Cloud Console, enable Gmail API, create an OAuth Desktop application, and download its client JSON as `credentials.json` in the project root.
3. Create a Telegram bot with BotFather. Start a chat with it and configure its token and chat ID.
4. Copy `.env.example` to `.env` and fill the required values.
5. Install dependencies:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

6. Authenticate and run:

```bash
python -m app.main auth
python -m app.main run-once
python -m app.main serve
```

The first authentication opens Google's OAuth consent flow. The generated `token.json` stays local and must never be committed.

## Configuration

Set `AI_PROVIDER=none`, `gemini`, or `openai`. Configure the matching API key for an external model. With `none`, the app uses local extraction as the summary fallback.

`GMAIL_QUERY` defaults to `newer_than:2d`. Adjust the Gmail search query in `.env` to control the mailbox window.

## Telegram commands

This initial version sends alerts automatically; interactive commands can be added in a later milestone.

## Safety

- Gmail scope is read-only. The app does not mark messages as read, archive, delete, or send email.
- Never commit `.env`, Google OAuth credentials, or token files.
- Do not forward OTPs, passwords, full account/card numbers, or secret authentication links to Telegram.
- Email content is untrusted input; the summarization prompt explicitly treats it as data, not instructions.
- Classification may be wrong. Review notifications and test with a limited mailbox query first.
