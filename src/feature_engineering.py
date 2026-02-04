import re

SCAM_KEYWORDS = ["registration fee", "instant offer", "whatsapp", "limited slots"]

def keyword_score(text):
    return sum(1 for k in SCAM_KEYWORDS if k in text.lower())

def is_free_email(email):
    return email.endswith(("@gmail.com", "@yahoo.com", "@outlook.com"))

def salary_flag(salary):
    return salary > 50000

