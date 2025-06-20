from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration headless de Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/chromium"

driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)

try:
    driver.get("http://127.0.0.1:5000")

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
    # Fermer le navigateur proprement
    driver.quit()
