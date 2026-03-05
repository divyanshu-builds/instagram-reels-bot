from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()

# small side window
options.add_argument("--window-size=400,700")
options.add_argument("--window-position=1200,50")

driver = webdriver.Chrome(options=options)

# open instagram
driver.get("https://www.instagram.com")
print("Login within 60 seconds...")
time.sleep(60)

# open reels page
driver.get("https://www.instagram.com/reels/")
time.sleep(6)

body = driver.find_element("tag name", "body")

count = 1

while True:

    # reel duration detect
    duration = driver.execute_script("""
    let vid = document.querySelector("video");
    if(vid){
        return vid.duration;
    }
    return 10;
    """)

    if duration is None or duration == float("inf"):
        duration = 10

    print("Watching reel", count, "for", duration, "seconds")

    time.sleep(duration)

    body.send_keys(Keys.ARROW_DOWN)

    count += 1
    time.sleep(2)