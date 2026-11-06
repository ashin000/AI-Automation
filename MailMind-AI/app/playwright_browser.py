"""Playwright helper for authorized browser automation.

Gmail reading is performed through Gmail's read-only API. This helper is kept
separate for browser workflows and smoke tests; it does not collect passwords.
"""
from playwright.sync_api import sync_playwright
from app.config import settings

def page_title(url: str) -> str:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=settings.playwright_headless)
        try:
            page = browser.new_page()
            page.goto(url, wait_until='domcontentloaded', timeout=30000)
            return page.title()
        finally:
            browser.close()
