from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_airdrops():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

    driver = webdriver.Chrome(options=options)

    url = "https://airdrops.io/active/"
    driver.get(url)

    airdrops = []

    try:
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.media-body")))

        cards = driver.find_elements(By.CSS_SELECTOR, 'div.media-body')

        for card in cards:
            try:
                title_elem = card.find_element(By.TAG_NAME, 'h3')
                desc_elem = card.find_element(By.TAG_NAME, 'p')
                link_elem = card.find_element(By.XPATH, './../../..')

                airdrops.append({
                    'title': title_elem.text.strip(),
                    'token': "?",  # site não exibe token diretamente
                    'date': "Unknown",  # também não mostra data de término
                    'description': desc_elem.text.strip(),
                    'link': link_elem.get_attribute('href'),
                    'source': 'airdrops.io'
                })

            except Exception as e:
                print("Error parsing card:", e)
                continue

    except Exception as e:
        print("[airdrops.io] Page load failed:", e)

    driver.quit()
    return airdrops


# Debug/test runner
if __name__ == "__main__":
    from pprint import pprint
    pprint(get_airdrops())
