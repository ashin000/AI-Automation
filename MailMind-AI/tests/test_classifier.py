import unittest
from app.classifier import classify_email

class ClassifierTests(unittest.TestCase):
    def test_bank_alert(self):
        result = classify_email({'from': 'alerts@bank.example', 'subject': 'UPI debit', 'snippet': 'INR 500 debited'})
        self.assertEqual(result.category, 'BANK_ALERT')

    def test_tldr_newsletter(self):
        result = classify_email({'from': 'TLDR newsletter', 'subject': 'Daily tech briefing'})
        self.assertEqual(result.category, 'TLDR_NEWSLETTER')

    def test_security_has_priority(self):
        result = classify_email({'subject': 'New login attempt - OTP'})
        self.assertEqual(result.category, 'SECURITY_ALERT')

if __name__ == '__main__':
    unittest.main()
