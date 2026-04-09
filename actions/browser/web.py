from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = None


# ---------------------------
# DRIVER HANDLING
# ---------------------------
def get_driver():
    global driver

    try:
        if driver:
            _ = driver.title
            return driver
    except:
        print("[Browser]: Old session invalid. Restarting...")
        driver = None

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    print("[Browser]: New Chrome session started")
    return driver


# ---------------------------
# BRING WINDOW TO FRONT
# ---------------------------
def bring_to_front():
    try:
        import pyautogui
        pyautogui.click(200, 200)  # simple reliable focus
        time.sleep(0.3)
    except:
        pass


# ---------------------------
# OPEN URL
# ---------------------------
def open_url(url):
    try:
        d = get_driver()

        d.get(url)
        bring_to_front()

        return f"Opened {url}"

    except Exception as e:
        print("[Browser Error]:", e)
        return None


# ---------------------------
# SEARCH FUNCTION (FIXED)
# ---------------------------
def search(query):
    try:
        d = get_driver()
        wait = WebDriverWait(d, 10)

        current_url = d.current_url.lower()

        # ---------------------------
        # AMAZON SEARCH (FULLY FIXED)
        # ---------------------------
        if "amazon" in current_url:

            # wait for page to fully load
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

            # wait until search box is clickable
            box = wait.until(
                EC.element_to_be_clickable((By.ID, "twotabsearchtextbox"))
            )

            box.click()
            time.sleep(0.5)  # stability

            box.clear()
            box.send_keys(query)
            box.send_keys(Keys.RETURN)

            return f"Searched Amazon for {query}"

        # ---------------------------
        # GOOGLE FALLBACK
        # ---------------------------
        else:
            d.get("https://www.google.com")

            box = wait.until(
                EC.presence_of_element_located((By.NAME, "q"))
            )

            box.clear()
            box.send_keys(query)
            box.send_keys(Keys.RETURN)

            return f"Searched Google for {query}"

    except Exception as e:
        print("[Search Error]:", e)
        return None