# # from actions.browser.web import get_driver, bring_to_front
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # import time

# # def open_youtube():
# #     try:
# #         d = get_driver()
# #         d.execute_script("window.open('https://www.youtube.com', '_blank');")
# #         time.sleep(0.5)
# #         d.switch_to.window(d.window_handles[-1])
# #         d.maximize_window()
# #         bring_to_front()
# #         return "Opened YouTube"
# #     except Exception as e:
# #         print(f"[YouTube Error]: {e}")
# #         return None

# # def search(query):
# #     try:
# #         d = get_driver()
# #         d.execute_script("window.open('https://www.youtube.com', '_blank');")
# #         time.sleep(1)
# #         d.switch_to.window(d.window_handles[-1])
# #         d.maximize_window()
# #         bring_to_front()
# #         time.sleep(1.5)
# #         box = d.find_element(By.NAME, "search_query")
# #         box.clear()
# #         box.send_keys(query)
# #         box.send_keys(Keys.RETURN)
# #         return f"Searched YouTube for {query}"
# #     except Exception as e:
# #         print(f"[YouTube Error]: {e}")
# #         return None

# # from actions.browser.web import get_driver, bring_to_front
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # import time

# # def open_youtube():
# #     try:
# #         d = get_driver()

# #         d.execute_script("window.open('https://www.youtube.com', '_blank');")
# #         time.sleep(0.5)

# #         d.switch_to.window(d.window_handles[-1])
# #         d.maximize_window()

# #         bring_to_front()

# #         return "Opened YouTube"

# #     except Exception as e:
# #         print("[YouTube Error]:", e)
# #         return None


# # def search(query):
# #     try:
# #         d = get_driver()

# #         d.execute_script("window.open('https://www.youtube.com', '_blank');")
# #         time.sleep(1)

# #         d.switch_to.window(d.window_handles[-1])
# #         d.maximize_window()
# #         bring_to_front()

# #         time.sleep(2)

# #         box = d.find_element(By.NAME, "search_query")
# #         box.clear()
# #         box.send_keys(query)
# #         box.send_keys(Keys.RETURN)

# #         return f"Searched YouTube for {query}"

# #     except Exception as e:
# #         print("[YouTube Error]:", e)
# #         return None

# # from actions.browser.web import get_driver, bring_to_front
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # import time


# # def open_youtube():
# #     try:
# #         d = get_driver()

# #         d.execute_script("window.open('https://www.youtube.com', '_blank');")
# #         time.sleep(1)

# #         d.switch_to.window(d.window_handles[-1])
# #         d.maximize_window()
# #         bring_to_front()

# #         return "Opened YouTube"

# #     except Exception as e:
# #         print("[YouTube Error]:", e)
# #         return None


# # def search(query):
# #     try:
# #         d = get_driver()

# #         d.execute_script("window.open('https://www.youtube.com', '_blank');")
# #         time.sleep(2)

# #         d.switch_to.window(d.window_handles[-1])
# #         d.maximize_window()
# #         bring_to_front()

# #         time.sleep(2)

# #         box = d.find_element(By.NAME, "search_query")
# #         box.clear()
# #         box.send_keys(query)
# #         box.send_keys(Keys.RETURN)

# #         return f"Searched YouTube for {query}"

# #     except Exception as e:
# #         print("[YouTube Error]:", e)
# #         return None


# # # ✅ ADD THIS FUNCTION (MISSING PIECE)
# # def play_first_video():
# #     try:
# #         d = get_driver()

# #         time.sleep(3)  # wait for results

# #         # safer selector
# #         videos = d.find_elements(By.CSS_SELECTOR, "a#video-title")

# #         if videos:
# #             videos[0].click()
# #             return "Playing video"
# #         else:
# #             return "No video found"

# #     except Exception as e:
# #         print("[YouTube Play Error]:", e)
# #         return None

# from actions.browser.web import get_driver, bring_to_front
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def open_youtube():
#     try:
#         d = get_driver()

#         d.execute_script("window.open('https://www.youtube.com', '_blank');")

#         d.switch_to.window(d.window_handles[-1])
#         d.maximize_window()
#         bring_to_front()

#         return "Opened YouTube"

#     except Exception as e:
#         print("[YouTube Error]:", e)
#         return None


# def search(query):
#     try:
#         d = get_driver()

#         d.execute_script("window.open('https://www.youtube.com', '_blank');")

#         d.switch_to.window(d.window_handles[-1])
#         d.maximize_window()
#         bring_to_front()

#         wait = WebDriverWait(d, 10)

#         box = wait.until(
#             EC.presence_of_element_located((By.NAME, "search_query"))
#         )

#         box.clear()
#         box.send_keys(query)
#         box.send_keys(Keys.RETURN)

#         return f"Searched YouTube for {query}"

#     except Exception as e:
#         print("[YouTube Error]:", e)
#         return None


# def play_first_video():
#     try:
#         d = get_driver()

#         wait = WebDriverWait(d, 10)

#         videos = wait.until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a#video-title"))
#         )

#         if videos:
#             videos[0].click()
#             return "Playing video"
#         else:
#             return "No video found"

#     except Exception as e:
#         print("[YouTube Play Error]:", e)
#         return None

from actions.browser.web import get_driver, bring_to_front
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def open_youtube():
    try:
        d = get_driver()
        d.execute_script("window.open('https://www.youtube.com', '_blank');")
        time.sleep(0.5)
        d.switch_to.window(d.window_handles[-1])
        d.maximize_window()
        bring_to_front()
        return "Opened YouTube"
    except Exception as e:
        print(f"[YouTube Error]: {e}")
        return None

def search(query):
    try:
        d = get_driver()
        d.execute_script("window.open('https://www.youtube.com', '_blank');")
        time.sleep(0.5)
        d.switch_to.window(d.window_handles[-1])
        d.maximize_window()
        bring_to_front()
        time.sleep(2)

        # search
        box = WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        box.clear()
        box.send_keys(query)
        box.send_keys(Keys.RETURN)
        time.sleep(3)

        # click first video
        first_video = WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer #thumbnail"))
        )
        first_video.click()
        time.sleep(2)

        return f"Playing {query} on YouTube"

    except Exception as e:
        print(f"[YouTube Error]: {e}")
        return None