import email
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
import os

def parse_eml(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    sender = msg['from']
    subject = msg['subject']
    body = ''
    links = []
    attachments = []

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            filename = part.get_filename()
            if filename:
                attachments.append(filename)
            if content_type == 'text/html':
                html = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                soup = BeautifulSoup(html, 'html.parser')
                body = soup.get_text()
                links = [a['href'] for a in soup.find_all('a', href=True)]
    else:
        body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

    return {
        "from": sender,
        "subject": subject,
        "body": body,
        "links": links,
        "attachments": attachments
    }
