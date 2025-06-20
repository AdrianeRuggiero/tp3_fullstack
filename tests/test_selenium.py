from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:5000")  # Assure-toi que Flask est en cours d'exécution

# Trouver les champs de saisie avec les bons IDs
input_a = driver.find_element(By.ID, "a")
input_b = driver.find_element(By.ID, "b")

# Remplir les champs
input_a.send_keys("5")
input_b.send_keys("10")

# Cliquer sur le bouton
button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

# Attendre le résultat
time.sleep(2)

# Vérifier le résultat
result = driver.find_element(By.ID, "result")
print("Résultat affiché :", result.text)

# Fermer le navigateur
driver.quit()
