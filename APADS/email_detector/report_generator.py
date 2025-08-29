import json
import os

def generate_report(report_data, filename="dashboard/reports/email_report.json"):
   # os.makedirs("reports", exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(report_data, f, indent=4)
    print(f"✅ Report saved to {filename}")
