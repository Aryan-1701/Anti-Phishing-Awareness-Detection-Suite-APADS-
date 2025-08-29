import tldextract
import re
import whois
from datetime import datetime

def analyze_domain(url):
    result = {
        "url": url,
        "domain": None,
        "suspicious_keywords": [],
        "ip_based": False,
        "domain_age_days": None
    }

    # Extract domain
    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}"
    result["domain"] = domain

    # Check for IP-based URLs
    if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", url):
        result["ip_based"] = True

    # Suspicious keywords in domain
    suspicious_words = ["login", "secure", "account", "update", "verify"]
    for word in suspicious_words:
        if word in domain.lower():
            result["suspicious_keywords"].append(word)

    # Domain WHOIS info
    try:
        info = whois.whois(domain)
        if info and info.creation_date:
            creation_date = info.creation_date
            if isinstance(creation_date, list):  # Sometimes WHOIS returns list
                creation_date = creation_date[0]
            age_days = (datetime.now() - creation_date).days
            result["domain_age_days"] = age_days
    except Exception as e:
        result["whois_error"] = str(e)

    return result
