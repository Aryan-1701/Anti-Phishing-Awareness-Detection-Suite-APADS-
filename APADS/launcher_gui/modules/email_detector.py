import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL_DIR = os.path.join(BASE_DIR, "..", "email_detector")

def main():
    print("Running URL Analyzer...")
    print("Starting Dashboard...")

    subprocess.run([sys.executable, os.path.join(EMAIL_DIR, "main.py")])

if __name__ == "__main__":
    main()
