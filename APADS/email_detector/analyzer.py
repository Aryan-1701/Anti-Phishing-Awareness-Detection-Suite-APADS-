import tldextract
import whois
import re
from datetime import datetime

def analyze_email(parsed_email):
    sender = parsed_email.get("from")
    links = parsed_email.get("links", [])
    attachments = parsed_email.get("attachments", [])

    is_suspicious_domain, domain = check_suspicious_domain(sender)
    suspicious_links = check_link_domains(links)
    domain_age = check_domain_age(domain) if domain else None
    score, verdict = score_email(domain, suspicious_links, attachments, domain_age)

    return {
        "from": sender,
        "subject": parsed_email.get("subject"),
        "suspicious_domain": domain,
        "suspicious_links": suspicious_links,
        "attachments": attachments,
        "domain_age_days": domain_age,
        "score": score,
        "verdict": verdict
    }


def check_suspicious_domain(sender_email):
    if sender_email:
        domain = sender_email.split('@')[-1]
        if any(w in domain for w in ['secure', 'login', 'verify', 'update']):
            return True, domain
    return False, None

def check_link_domains(links):
    suspicious_links = []
    for link in links:
        ext = tldextract.extract(link)
        domain = f"{ext.domain}.{ext.suffix}"
        if re.search(r"\d+\.\d+\.\d+\.\d+", link):  # IP in URL
            suspicious_links.append(link)
        elif any(w in domain for w in ['secure', 'login', 'verify', 'account']):
            suspicious_links.append(link)
    return suspicious_links

def check_domain_age(domain):
    try:
        w = whois.whois(domain)
        if isinstance(w.creation_date, list):
            creation_date = w.creation_date[0]
        else:
            creation_date = w.creation_date
        if creation_date:
            age = (datetime.now() - creation_date).days
            return age
    except:
        return None
    return None

def score_email(sender_domain, suspicious_links, attachments, domain_age):
    score = 0
    if sender_domain: score += 2
    if suspicious_links: score += 2
    if any(a.endswith(('.exe', '.js', '.scr', '.zip', '.docm')) for a in attachments):
        score += 3
    if domain_age is not None and domain_age < 180:
        score += 2

    if score >= 6:
        verdict = "PHISHING"
    elif score >= 3:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"
    return score, verdict
