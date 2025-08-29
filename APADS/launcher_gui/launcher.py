import tkinter as tk
import subprocess
import webbrowser
import os
import sys
import time

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "modules")

def run_email_detector():
    subprocess.run([sys.executable, os.path.join(MODULES_DIR, "email_detector.py")])

def run_url_analyzer():
    subprocess.run([sys.executable, os.path.join(MODULES_DIR, "url_analyzer.py")])

def run_dashboard():
    subprocess.Popen([sys.executable, os.path.join(MODULES_DIR, "dashboard_runner.py")])
    time.sleep(2)  # give Flask time to start
    webbrowser.open("http://127.0.0.1:5000")

# --- GUI Setup ---
root = tk.Tk()
root.title("APADS Launcher")
root.geometry("350x250")

tk.Label(root, text="APADS Launcher", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(root, text="Email Detector", width=25, command=run_email_detector).pack(pady=5)
tk.Button(root, text="URL Analyzer", width=25, command=run_url_analyzer).pack(pady=5)
tk.Button(root, text="Open Dashboard", width=25, command=run_dashboard).pack(pady=5)

tk.Button(root, text=" Exit", width=25, command=root.quit).pack(pady=20)

root.mainloop()
