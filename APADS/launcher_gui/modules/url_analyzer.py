import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL_DIR = os.path.join(BASE_DIR, "..", "url_analyzer")

def main():
    print("Running URL Analyzer...")
    url = input("Enter a URL to analyze: ").strip()
    if url:
        subprocess.run([sys.executable, os.path.join(URL_DIR, "main.py"), url])
    else:
        print("No URL entered.")

if __name__ == "__main__":
    main()
