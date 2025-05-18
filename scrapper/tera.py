from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import json


def extractData():
    productCards = driver.find_elements(By.CLASS_NAME, "product-item__box")

    pageData = []
    url = driver.current_url
    print(f"Extracting from {url}")
    for productCard in productCards:
        name = productCard.find_element(
            By.CLASS_NAME, "product-item__name").get_attribute("title")
        product_url = productCard.find_element(
            By.CLASS_NAME, "product-item__name").get_attribute("href")

        try:
            img_src = productCard.find_element(
                By.CLASS_NAME, "image-thumbnail").get_attribute("src")
        except:
            img_src = None

        oldPrice = productCard.find_element(
            By.CSS_SELECTOR,
            "div.product-item__old-price del span"
        ).text
        currentPrice = productCard.find_element(
            By.CSS_SELECTOR,
            "div.product-item__new-price > span"
        ).text

        productData = {"loja": "TerabyteShop", "name": name, "img_src": img_src, "product_url": product_url, "active_sale": True if oldPrice else False, "old_price": oldPrice if oldPrice else None,
                       "price": currentPrice, "url": url, "date": datetime.today().strftime('%Y-%m-%d')}

        pageData.append(productData)

    return pageData


def navigateToNextPage():
    nextButton = driver.find_element(By.CLASS_NAME, "btn-pdmore")
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", nextButton)
    time.sleep(0.5)
    nextButton.click()


options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get("https://www.terabyteshop.com.br/hardware")

title = driver.title




time.sleep(5)
modal = driver.find_element(By.CLASS_NAME, "modal")
modalClose =  modal.find_element(By.CSS_SELECTOR, "button.close > span")
modalClose.click()

consentButton = driver.find_element(By.ID, "submitFormContinuar")
consentButton.click()

data = []

pagesCount = 0
while True:

    pageData = extractData()
    data.extend(pageData)

    wait = WebDriverWait(driver, timeout=100)

    #try:
    navigateToNextPage()
    #except:
    #    print("last page reached")
    #    break

    # WebDriverWait(driver, 5*60).until(EC.url_changes(driver.current_url))
    #WebDriverWait(driver, 30).until(
    #    EC.presence_of_element_located((By.CLASS_NAME, "productCard"))
    #)
    pagesCount += 1
    if pagesCount >= 2:
        break

finish_time = datetime.now()
timestamp = finish_time.strftime("%Y-%m-%d_%H-%M")

with open(f"products_tera_{timestamp}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

driver.quit()
