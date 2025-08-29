import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DASHBOARD_DIR = os.path.join(BASE_DIR, "..", "dashboard")

def main():
    print("Running URL Analyzer...")
    print("Starting Dashboard...")
    subprocess.run([sys.executable, os.path.join(DASHBOARD_DIR, "app.py")])

if __name__ == "__main__":
    main()
