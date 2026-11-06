import re
from dataclasses import dataclass

@dataclass
class Classification:
    category: str
    priority: str
    reason: str

SECURITY = re.compile(r'otp|one.time.password|login attempt|new sign.?in|password reset|security alert|suspicious', re.I)
BANK = re.compile(r'bank|account|upi|transaction|debited|credited|withdraw|deposit|statement|card', re.I)
TLDR = re.compile(r'tldr|the rundown|newsletter|daily tech', re.I)

def classify_email(email: dict) -> Classification:
    text = ' '.join(str(email.get(k, '')) for k in ('from', 'subject', 'snippet', 'body'))
    if SECURITY.search(text):
        return Classification('SECURITY_ALERT', 'CRITICAL', 'Possible account security/authentication alert')
    if BANK.search(text):
        return Classification('BANK_ALERT', 'HIGH', 'Financial or transaction-related content')
    if TLDR.search(text):
        return Classification('TLDR_NEWSLETTER', 'NORMAL', 'Newsletter pattern matched')
    return Classification('OTHER', 'LOW', 'No configured important-mail pattern matched')
