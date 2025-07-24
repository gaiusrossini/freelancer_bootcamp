from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_airdrops():
    options = Options()
    options.add_argument('--headless')  # Remove this line to see browser
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    driver.get('https://coinmarketcap.com/airdrop/')

    time.sleep(8)

    airdrops = []

    cards = driver.find_elements(By.CSS_SELECTOR, 'div[class*="aairdropCard"]')

    for card in cards:
        try:
            title = card.find_element(By.CSS_SELECTOR, 'h3').text.strip()
            token = card.find_element(By.CSS_SELECTOR, 'span[class*="name"]').text.strip()
            date = card.find_element(By.CSS_SELECTOR, 'span[class*="date"]').text.strip()
            link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')

            airdrops.append({
                'title': title,
                'token': token,
                'date': date,
                'link': f"https://coinmarketcap.com{link}" if link.startswith("/") else link,
                'source': 'coinmarketcap'
            })
        except Exception as e:
            print("Error parsing card:", e)
            continue

    driver.quit()
    return airdrops

# Debug mode (optional)
if __name__ == "__main__":
    from pprint import pprint
    pprint(get_airdrops())
