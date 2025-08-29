from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def capture_screenshot(url):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(url)
        path = os.path.join("report", "site_capture.png")
        driver.save_screenshot(path)
        driver.quit()
        return path
    except Exception as e:
        return None
