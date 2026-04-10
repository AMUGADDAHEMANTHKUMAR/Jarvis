from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import time

driver = None

def get_driver():
    global driver
    if driver is None:
        try:
            options = Options()
            options.add_argument("--start-maximized")
            options.add_argument("--foreground")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            print("[Browser]: New Chrome session started")
        except Exception as e:
            print(f"[Browser Error]: {e}")
            driver = None
    else:
        try:
            _ = driver.title
        except:
            print("[Browser]: Old session invalid. Restarting...")
            driver = None
            return get_driver()
    return driver

def bring_to_front():
    try:
        d = get_driver()
        d.maximize_window()
    except:
        pass

def open_url(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url
        d = get_driver()
        d.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(0.5)
        d.switch_to.window(d.window_handles[-1])
        d.maximize_window()
        bring_to_front()
        return f"Opened {url}"
    except Exception as e:
        print(f"[Browser Error]: {e}")
        return None

def search_on_page(query):
    try:
        d = get_driver()
        # try to find search box on current page
        try:
            search_box = WebDriverWait(d, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                    "input[type='search'], input[name='q'], input[name='search'], input[id='twotabsearchtextbox'], input[placeholder*='Search'], input[placeholder*='search']"
                ))
            )
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)
            return f"Searched for {query}"
        except:
            # fallback to google search
            d.execute_script(f"window.open('https://www.google.com/search?q={query}', '_blank');")
            d.switch_to.window(d.window_handles[-1])
            return f"Googled {query}"
    except Exception as e:
        print(f"[Browser Error]: {e}")
        return None
