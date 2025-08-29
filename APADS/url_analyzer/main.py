import json
import sys
from domain_analysis import analyze_domain
from html_analysis import analyze_html
from screenshot import capture_screenshot
from utils.safe_browsing_api import check_url_reputation

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        return

    url = sys.argv[1]
    print(f"Scanning URL: {url}")

    report = {}
    # Domain & URL checks
    report.update(analyze_domain(url))

    # HTML content analysis
    report.update(analyze_html(url))

    # Screenshot (optional)
    screenshot_path = capture_screenshot(url)
    if screenshot_path:
        report["screenshot"] = screenshot_path

    # Reputation check (Google Safe Browsing / VirusTotal API stub)
    rep_check = check_url_reputation(url)
    report.update(rep_check)

    # Save to report file
    with open("report/result.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Scan complete. Report saved at report/result.json")

if __name__ == "__main__":
    main()
