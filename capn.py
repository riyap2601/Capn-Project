import imaplib
import email
import re
import pandas as pd
from datetime import datetime
import os
import json
import gzip
import time

user = "reports@capnapp.com"
app_password = "tzar siap yccu snbo"

app_password = app_password.replace(" ", "")

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(user, app_password)
mail.select("inbox")

print("Connected successfully!")

status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()[-5:]

print(f"\nFound {len(messages[0].split())} total emails")
print("\nLast 5 email subjects:")

for email_id in email_ids:
    status, data = mail.fetch(email_id, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])
    print(f"  - {msg['Subject']}")

mail.close()
mail.logout()

