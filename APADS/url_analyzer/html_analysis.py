import requests
from bs4 import BeautifulSoup

def analyze_html(url):
    result = {
        "has_login_form": False,
        "external_form_actions": [],
        "password_fields": 0
    }

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")

        # Look for forms
        forms = soup.find_all("form")
        for form in forms:
            action = form.get("action")
            if action and not url in action:
                result["external_form_actions"].append(action)

        # Count password fields
        password_fields = soup.find_all("input", {"type": "password"})
        result["password_fields"] = len(password_fields)
        if result["password_fields"] > 0:
            result["has_login_form"] = True

    except Exception as e:
        result["html_error"] = str(e)

    return result
