from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_airdrops():
    """
    Scrapes airdrops from airdrops.io main page using Selenium.

    Returns:
        list: A list of dictionaries containing airdrop data.
    """
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    driver.get("https://airdrops.io/")

    airdrops = []

    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.col-lg-4')))

        cards = driver.find_elements(By.CSS_SELECTOR, 'div.col-lg-4')

        for card in cards:
            try:
                link_elem = card.find_element(By.CSS_SELECTOR, 'a')
                link = link_elem.get_attribute('href').strip()
                title = link_elem.text.strip()

                airdrops.append({
                    'title': title,
                    'token': '?',
                    'date': '?',
                    'link': link,
                    'source': 'airdrops.io'
                })

            except Exception as e:
                print(f"[airdrops.io] Error parsing card: {repr(e)}")
                continue

    except Exception as e:
        print(f"[airdrops.io] Timeout or loading error: {repr(e)}")

    driver.quit()
    return airdrops


# Debug mode
if __name__ == "__main__":
    from pprint import pprint
    pprint(get_airdrops())
