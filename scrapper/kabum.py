from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

driver = webdriver.Chrome()

driver.get("https://www.kabum.com.br/hardware")

title = driver.title

productCards = driver.find_elements(By.CLASS_NAME, "productCard")

data = []
url = driver.current_url
for productCard in productCards:
    name = productCard.find_element(By.CLASS_NAME, "nameCard").text
    oldPrice = productCard.find_element(By.CLASS_NAME, "oldPriceCard").text
    currentPrice = productCard.find_element(By.CLASS_NAME, "priceCard").text

    productData = {"name": name, "active_sale": True if oldPrice else False, "old_price": oldPrice if oldPrice else None,
                   "price": currentPrice, "url": url, "date": datetime.today().strftime('%Y-%m-%d')}

    data.append(productData)

print(data)

driver.quit()
