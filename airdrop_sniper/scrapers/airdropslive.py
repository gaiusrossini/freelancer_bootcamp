from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

options = Options()
# options.add_argument('--headless')  # Ative se quiser sem abrir navegador
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(options=options)

url = "https://airdrops.live/"
driver.get(url)

airdrops = []

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.airdrop-item')))

    cards = driver.find_elements(By.CSS_SELECTOR, 'div.airdrop-item')

    for card in cards:
        try:
            link_elem = card.find_element(By.TAG_NAME, 'a')
            link = link_elem.get_attribute('href')

            title = link.split('/')[-2].replace('-', ' ').title()

            # Descrição opcional (se quiser adicionar isso depois)
            # desc = card.find_element(By.TAG_NAME, 'p').text.strip()

            airdrops.append({
                'title': title,
                'token': '?',
                'date': '?',
                'link': link,
                'source': 'airdrops.live'
            })
        except Exception as e:
            print("[airdrops.live] Erro ao processar card:", e)
            continue

except Exception as e:
    print("[airdrops.live] Timeout ou falha ao carregar cards:", e)

driver.quit()

# Exibir
print(json.dumps(airdrops, indent=2, ensure_ascii=False))
