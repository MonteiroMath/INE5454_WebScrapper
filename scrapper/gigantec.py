from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import json


def extractData():
    productCards = driver.find_elements(
        By.CLASS_NAME, "product-item-info")

    pageData = []
    url = driver.current_url
    print(f"Extracting from {url}")
    for productCard in productCards:
        name = productCard.find_element(
            By.CLASS_NAME, "product-item-link").text

        try:
            img_src = productCard.find_element(
                By.TAG_NAME, "img").get_attribute("src")
        except:
            img_src = None

        try:
            oldPrice = productCard.find_element(
                By.CSS_SELECTOR, 'span[id^="old-price-"]').get_attribute('data-price-amount')
        except:
            oldPrice = None

        try:
            currentPrice = productCard.find_element(
                By.CSS_SELECTOR, 'span[id^="avista-price-"]').get_attribute('data-price-amount')
        except:
            currentPrice = None

        productData = {"loja": "Gigantec", "name": name, "img": img_src, "active_sale": True if oldPrice else False, "old_price": oldPrice if oldPrice else None,
                       "price": currentPrice, "url": url, "date": datetime.today().strftime('%Y-%m-%d')}

        pageData.append(productData)

    return pageData


def navigateToNextPage():
    nextButton = driver.find_element(
        By.CLASS_NAME, "pages-item-next")
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth'});", nextButton)
    time.sleep(0.5)
    nextButton.click()


options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get("https://www.gigantec.com.br/hardware-pecas.html")

title = driver.title

data = []

# consentButton = driver.find_element(By.ID, "aceitar-uso-cookies")
# consentButton.click()

pagesCount = 0
while True:

    pageData = extractData()

    data.extend(pageData)

    wait = WebDriverWait(driver, timeout=100)

    try:
        navigateToNextPage()
    except:
        print("last page reached")
        break

    WebDriverWait(driver, 5*60).until(EC.url_changes(driver.current_url))
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "product-item-info"))
    )

    pagesCount += 1
    if pagesCount >= 50:
        break

finish_time = datetime.now()
timestamp = finish_time.strftime("%Y-%m-%d_%H-%M")

with open(f"data/products_gigantec_{timestamp}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

driver.quit()
