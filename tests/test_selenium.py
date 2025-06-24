from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configuration headless de Chrome pour Docker
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Utiliser le chromedriver installé dans l'image Docker
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

try:
    time.sleep(5)  # Attendre le démarrage de l'API Flask

    # 🔧 Adresse interne du service Flask (même réseau Docker)
    driver.get("http://flask-app:5000")

    # Trouver les champs de saisie avec les bons IDs
    input_a = driver.find_element(By.ID, "a")
    input_b = driver.find_element(By.ID, "b")

    # Remplir les champs
    input_a.send_keys("5")
    input_b.send_keys("10")

    # Cliquer sur le bouton
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Attendre que le résultat apparaisse
    time.sleep(2)

    # Vérifier le résultat
    result = driver.find_element(By.ID, "result")
    print("Résultat affiché :", result.text)

finally:
    driver.quit()
