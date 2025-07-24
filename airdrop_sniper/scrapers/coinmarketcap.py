from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

# Browser settings
options = Options()
# Uncomment the line below to run in headless mode (no browser window)
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0")

# Start the Chrome driver
driver = webdriver.Chrome(options=options)

# Open the CoinMarketCap airdrops page
url = 'https://coinmarketcap.com/airdrop/'
driver.get(url)

# Wait for the page to fully load
time.sleep(8)  # You can increase if your connection is slow

airdrops = []

# Find all airdrop cards
cards = driver.find_elements(By.CSS_SELECTOR, 'div[class*="aairdropCard"]')

for card in cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, 'h3').text.strip()
        token = card.find_element(By.CSS_SELECTOR, 'span[class*="name"]').text.strip()
        date = card.find_element(By.CSS_SELECTOR, 'span[class*="date"]').text.strip()
        link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')

        # Append to the list
        airdrops.append({
            'title': title,
            'token': token,
            'date': date,
            'link': f"https://coinmarketcap.com{link}" if link.startswith("/") else link
        })
    except Exception as e:
        print("Error parsing card:", e)
        continue

driver.quit()

# Print results as formatted JSON
print(json.dumps(airdrops, indent=2, ensure_ascii=False))
