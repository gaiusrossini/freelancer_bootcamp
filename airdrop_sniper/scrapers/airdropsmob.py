from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def get_airdrops():
    """
    Scrapes airdrops from airdropsmob.com using Selenium.

    Returns:
        list: A list of dictionaries containing airdrop data.
    """
    WAIT_TIME = 10  # seconds

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    driver.get("https://airdropsmob.com/")

    time.sleep(WAIT_TIME)

    airdrops = []

    cards = driver.find_elements(By.CSS_SELECTOR, "div.post_container")
    for card in cards:
        try:
            link_elem = card.find_element(By.CSS_SELECTOR, 'div.logo_post a')
            title = link_elem.get_attribute("title").strip()
            link = link_elem.get_attribute("href").strip()

            token_elem = card.find_element(By.CSS_SELECTOR, 'div.value_wrapper')
            raw_token = token_elem.text.strip().split('\n')
            token = raw_token[0] if raw_token else "?"

            date_elem = card.find_element(By.CSS_SELECTOR, 'div.botuni_wrapper')
            raw_date = date_elem.text.strip().split('\n')
            date = raw_date[-1] if raw_date else "?"

            airdrops.append({
                "title": title,
                "token": token,
                "date": date,
                "link": link,
                "source": "airdropsmob"
            })

        except Exception as e:
            print(f"[ERROR] Failed to parse a card: {repr(e)}")
            continue

    driver.quit()
    return airdrops


# Debug mode
if __name__ == "__main__":
    from pprint import pprint
    pprint(get_airdrops())
