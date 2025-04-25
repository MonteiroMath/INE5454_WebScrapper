from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get("https://www.kabum.com.br/hardware")

title = driver.title

productCards = driver.find_elements(By.CLASS_NAME, "productCard")

consentButton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
consentButton.click()

data = []
url = driver.current_url
for productCard in productCards:
    name = productCard.find_element(By.CLASS_NAME, "nameCard").text
    oldPrice = productCard.find_element(By.CLASS_NAME, "oldPriceCard").text
    currentPrice = productCard.find_element(By.CLASS_NAME, "priceCard").text

    productData = {"name": name, "active_sale": True if oldPrice else False, "old_price": oldPrice if oldPrice else None,
                   "price": currentPrice, "url": url, "date": datetime.today().strftime('%Y-%m-%d')}

    data.append(productData)


wait = WebDriverWait(driver, timeout=100)
nextButton = driver.find_element(By.CLASS_NAME, "nextLink")
driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", nextButton)
time.sleep(0.5)
nextButton.click()


driver.quit()
