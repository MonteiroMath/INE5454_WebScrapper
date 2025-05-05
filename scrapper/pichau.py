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
        By.CSS_SELECTOR, "[class*='product_item']")

    pageData = []
    url = driver.current_url
    print(f"Extracting from {url}")
    for productCard in productCards:
        name = productCard.find_element(
            By.CSS_SELECTOR, "[class*='product_info_title-noMarginBottom']").text

        try:
            img_src = productCard.find_element(
                By.TAG_NAME, "img").get_attribute("src")
        except:
            img_src = None

        try:
            oldPrice = productCard.find_element(
                By.CSS_SELECTOR, "[class*='strikeThrough']").text
        except:
            oldPrice = None

        try: 
            currentPrice = productCard.find_element(
                By.CSS_SELECTOR, "div[class*='price_vista']").text
        except:
            currentPrice = None

        productData = {"loja": "Pichau", "name": name, "img": img_src, "active_sale": True if oldPrice else False, "old_price": oldPrice if oldPrice else None,
                       "price": currentPrice, "url": url, "date": datetime.today().strftime('%Y-%m-%d')}

        pageData.append(productData)

    return pageData


def navigateToNextPage():
    nextButton = driver.find_element(
        By.CSS_SELECTOR, '[aria-label="Go to next page"]')
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", nextButton)
    time.sleep(0.5)
    nextButton.click()


options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get("https://www.pichau.com.br/hardware")

title = driver.title

data = []

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
            (By.CSS_SELECTOR, "[class*='product_info_title-noMarginBottom']"))
    )

    pagesCount += 1
    if pagesCount >= 50:
        break

finish_time = datetime.now()
timestamp = finish_time.strftime("%Y-%m-%d_%H-%M")

with open(f"products_pichau_{timestamp}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

driver.quit()
