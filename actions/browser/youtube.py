from actions.browser.web import get_driver, bring_to_front
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_youtube():
    try:
        d = get_driver()
        d.get("https://www.youtube.com")
        d.maximize_window()
        bring_to_front()
        return "Opened YouTube"
    except Exception as e:
        print(f"[YouTube Error]: {e}")
        return None


# ---------------------------
# SMART SEARCH (no autoplay)
# ---------------------------
def search(query):
    try:
        d = get_driver()
        d.get("https://www.youtube.com")
        bring_to_front()
        time.sleep(2)

        box = WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        box.clear()
        box.send_keys(query)
        box.send_keys(Keys.RETURN)

        return f"Searched YouTube for {query}"

    except Exception as e:
        print(f"[YouTube Error]: {e}")
        return None


# ---------------------------
# SMART PLAY (better video selection)
# ---------------------------
def play_first_video(video):
    try:
        d = get_driver()
        d.get("https://www.youtube.com")
        bring_to_front()
        time.sleep(2)

        # search
        box = WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        box.clear()
        box.send_keys(video)
        box.send_keys(Keys.RETURN)
        time.sleep(2)

        # scroll a bit → load better results
        for _ in range(2):
            d.execute_script("window.scrollBy(0, 600)")
            time.sleep(1)

        # pick a GOOD video (not ads/shorts)
        videos = WebDriverWait(d, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "ytd-video-renderer")
            )
        )

        for v in videos:
            try:
                title = v.find_element(By.ID, "video-title")
                if title.is_displayed():
                    title.click()
                    break
            except:
                continue

        return f"Playing {video} on YouTube"

    except Exception as e:
        print(f"[YouTube Play Error]: {e}")
        return None


# ---------------------------
# SHARE TO WHATSAPP (stable way)
# ---------------------------
def share_on_whatsapp():
    try:
        d = get_driver()
        current_url = d.current_url

        # open WhatsApp Web with message
        whatsapp_url = f"https://web.whatsapp.com/send?text={current_url}"
        d.execute_script(f"window.open('{whatsapp_url}', '_blank');")
        time.sleep(1)
        d.switch_to.window(d.window_handles[-1])
        bring_to_front()

        return "Opened WhatsApp share window"

    except Exception as e:
        print(f"[WhatsApp Share Error]: {e}")
        return None

