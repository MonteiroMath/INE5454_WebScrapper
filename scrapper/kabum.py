from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import json


def extractData():
    productCards = driver.find_elements(By.CLASS_NAME, "productCard")

    pageData = []
    url = driver.current_url
    print(f"Extracting from {url}")
    for productCard in productCards:
        name = productCard.find_element(By.CLASS_NAME, "nameCard").text

        try:
            img_src = productCard.find_element(
                By.TAG_NAME, "img").get_attribute("src")
        except:
            img_src = None

        oldPrice = productCard.find_element(By.CLASS_NAME, "oldPriceCard").text
        currentPrice = productCard.find_element(
            By.CLASS_NAME, "priceCard").text

        productData = {"loja": "kabum", "name": name, "img": img_src, "active_sale": True if oldPrice else False, "old_price": oldPrice if oldPrice else None,
                       "price": currentPrice, "url": url, "date": datetime.today().strftime('%Y-%m-%d')}

        pageData.append(productData)

    return pageData


def navigateToNextPage():
    nextButton = driver.find_element(By.CLASS_NAME, "nextLink")    
    driver.execute_script(
        "arguments[0].click();", nextButton)
    #nextButton.click()


options = Options()
#options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get("https://www.kabum.com.br/hardware")

title = driver.title

consentButton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
consentButton.click()
data = []

pagesCount = 0
while True:

    pageData = extractData()
    data.extend(pageData)

    wait = WebDriverWait(driver, timeout=100)


    navigateToNextPage()
    #try:
    #    navigateToNextPage()
    #except:
#
    #    print("last page reached")
    #    break

    WebDriverWait(driver, 5*60).until(EC.url_changes(driver.current_url))
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "productCard"))
    )
    pagesCount += 1
    if pagesCount >= 50:
        break

finish_time = datetime.now()
timestamp = finish_time.strftime("%Y-%m-%d_%H-%M")

with open(f"data/products_kabum_{timestamp}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

driver.quit()
