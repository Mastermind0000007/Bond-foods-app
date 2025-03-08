```
import hashlib
import logging
import re
from datetime import datetime, timedelta

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def log_error(message):
    logging.error(message)

def format_date(date):
    return date.strftime("%Y-%m-%d")

def calculate_expiration_date(days):
    return datetime.now() + timedelta(days=days)
```
