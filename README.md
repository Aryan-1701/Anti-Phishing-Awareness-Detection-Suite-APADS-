APADS – Advanced Phishing Awareness & Detection Suite

APADS (Advanced Phishing Awareness & Detection System) is a comprehensive cybersecurity tool designed to detect, analyze, and prevent phishing attacks. The system is built for educational and practical purposes, combining real-time email analysis, URL inspection, and awareness training into a unified dashboard. APADS helps users and organizations enhance cybersecurity hygiene by identifying phishing threats and providing actionable insights.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Key Features:
Detects phishing emails using content and metadata analysis
Analyzes suspicious URLs and attachments
Generates structured reports of threats detected
Simulates phishing scenarios for training and awareness
Provides a web-based dashboard for easy visualization of results

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Important Steps to Use

1. Clone the Repository
git clone <repository-url>
cd APADS


2. Install Dependencies
Ensure Python 3.x is installed, then install required libraries:
pip install -r requirements.txt


3. Set Up Folders
Place sample .eml emails in the email_detector/test_emails folder.
Ensure a reports folder exists in the email_detector directory to save analysis outputs.

4. Run Launcher GUI
The launcher provides a unified interface to run all modules:
python launcher_gui/launcher.py

From the launcher, you can start:

Email Detector – analyzes emails and generates JSON reports.

URL Analyzer – checks suspicious links for potential phishing.

Dashboard – displays phishing analysis results and simulations in a web interface.

View Reports

Generated reports are stored in the reports folder. Open the JSON files for detailed insights.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Advantages:
Comprehensive Protection: Detects phishing emails, malicious links, and suspicious attachments.
Awareness & Training: Simulates phishing scenarios to educate users.
Easy Visualization: Interactive dashboard for easy interpretation of reports.
Automated Reporting: Generates structured JSON reports for tracking and analysis.
Flexible & Scalable: Can analyze multiple emails and URLs simultaneously and can be integrated with other cybersecurity tools.
