import argparse
import time
from app.config import settings


def main():
    parser = argparse.ArgumentParser(description='MailMind AI email intelligence agent')
    parser.add_argument('command', choices=['auth', 'run-once', 'serve', 'browser-test'])
    parser.add_argument('--url', default='https://example.com')
    args = parser.parse_args()
    if args.command == 'auth':
        from app.gmail_client import authenticate
        authenticate()
        print('Gmail OAuth authentication successful.')
    elif args.command == 'browser-test':
        from app.playwright_browser import page_title
        print(page_title(args.url))
    else:
        from app.agent import run_agent
        if args.command == 'run-once':
            print(run_agent())
        else:
            print(f'Polling every {settings.poll_interval_minutes} minutes. Press Ctrl+C to stop.')
            while True:
                try:
                    print(run_agent())
                except Exception as exc:
                    print(f'Agent error: {type(exc).__name__}: {exc}')
                time.sleep(max(1, settings.poll_interval_minutes) * 60)

if __name__ == '__main__':
    main()
