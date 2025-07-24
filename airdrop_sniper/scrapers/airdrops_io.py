from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Configuração do navegador
options = Options()
# options.add_argument('--headless')  # não abre a janela
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(options=options)

url = "https://airdrops.io/active/"
driver.get(url)

# Espera até que os elementos estejam presentes (melhor que sleep fixo)
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.media-body")))

airdrops = []

cards = driver.find_elements(By.CSS_SELECTOR, 'div.media-body')
for card in cards:
    try:
        title = card.find_element(By.TAG_NAME, 'h3').text.strip()
        desc = card.find_element(By.TAG_NAME, 'p').text.strip()
        # O link está 3 níveis acima
        link = card.find_element(By.XPATH, './../../..').get_attribute('href')

        airdrops.append({
            'title': title,
            'description': desc,
            'link': link
        })
    except Exception as e:
        print("Erro em card:", e)
        continue

driver.quit()

# Exibir ou salvar os dados
print(json.dumps(airdrops, indent=2, ensure_ascii=False))
