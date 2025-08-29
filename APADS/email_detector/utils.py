import os
import re
import json
from datetime import datetime
from pathlib import Path

def extract_domain_from_email(email_address):
    """Returns domain from an email address"""
    if email_address and "@" in email_address:
        return email_address.split("@")[-1].strip().lower()
    return None

def extract_ip_from_url(url):
    """Checks if URL contains an IP address"""
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    match = re.search(pattern, url)
    return match.group() if match else None

def save_json_report(data, filename):
    """Saves dictionary to JSON file with timestamp"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"✅ JSON report saved to: {filename}")

def get_timestamped_filename(prefix="email_report", folder="reports"):
    """Generates a timestamped report filename"""
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(folder, f"{prefix}_{timestamp}.json")

def is_executable_attachment(filename):
    """Returns True if the attachment is a suspicious executable"""
    dangerous_exts = ('.exe', '.scr', '.bat', '.cmd', '.vbs', '.js', '.docm', '.zip')
    return filename.lower().endswith(dangerous_exts)

def read_file_content(filepath):
    """Safely reads a text or HTML file"""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def clean_text(text):
    """Strips and removes excessive whitespace"""
    return ' '.join(text.strip().split())
