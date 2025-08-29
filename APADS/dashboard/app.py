from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "replace_this_with_a_random_secret"  # only for flash messages in dev

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SIM_LOG = os.path.join(BASE_DIR, "phishing_emails", "simulation_log.txt")

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None

@app.route("/")
def index():
    # quick stats: counts of reports if present
    email_report = load_json(os.path.join(REPORTS_DIR, "email_report.json"))
    url_report = load_json(os.path.join(REPORTS_DIR, "url_report.json"))
    stats = {
        "email_exists": bool(email_report),
        "url_exists": bool(url_report)
    }
    return render_template("index.html", stats=stats)

@app.route("/reports")
def reports():
    email_report = load_json(os.path.join(REPORTS_DIR, "email_report.json"))
    url_report = load_json(os.path.join(REPORTS_DIR, "url_report.json"))
    return render_template("report.html", email=email_report, url=url_report)

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/api/reports")
def api_reports():
    """Return combined minimal stats for charting/JS usage."""
    email_report = load_json(os.path.join(REPORTS_DIR, "email_report.json"))
    url_report = load_json(os.path.join(REPORTS_DIR, "url_report.json"))

    # derive simple stats
    email_verdict = email_report.get("verdict") if email_report else None
    url_verdict = url_report.get("verdict") if url_report else None

    data = {
        "email": {
            "present": bool(email_report),
            "verdict": email_verdict,
            "score": email_report.get("score") if email_report else None
        },
        "url": {
            "present": bool(url_report),
            "verdict": url_verdict,
            "score": url_report.get("score") if url_report else None
        }
    }
    return jsonify(data)

@app.route("/simulate", methods=["GET", "POST"])
def simulate():
    """
    Simple simulation endpoint: logs a simulated phishing email attempt.
    NOTE: This does NOT send real emails. Use only for testing/awareness.
    """
    if request.method == "POST":
        target = request.form.get("target_email", "").strip()
        template = request.form.get("template", "Generic phishing simulation").strip()
        if not target:
            flash("Please provide an email address to simulate to.", "error")
            return redirect(url_for("simulate"))
        os.makedirs(os.path.dirname(SIM_LOG), exist_ok=True)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{ts} | target: {target} | template: {template}\n"
        with open(SIM_LOG, "a", encoding="utf-8") as f:
            f.write(entry)
        flash(f"Simulation logged for {target}. (Check simulation_log.txt)", "success")
        return redirect(url_for("simulate"))

    # GET
    # show last 10 entries of the log (if any)
    recent = []
    if os.path.exists(SIM_LOG):
        with open(SIM_LOG, "r", encoding="utf-8") as f:
            lines = f.readlines()
            recent = [l.strip() for l in lines[-10:]][::-1]
    return render_template("simulate.html", recent=recent)

if __name__ == "__main__":
    # create folders if missing to avoid runtime errors
    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "phishing_emails"), exist_ok=True)
    app.run(debug=True, port=5000)
