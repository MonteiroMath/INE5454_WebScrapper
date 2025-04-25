from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


def extractData():
    productCards = driver.find_elements(By.CLASS_NAME, "productCard")

    pageData = []
    url = driver.current_url
    for productCard in productCards:
        name = productCard.find_element(By.CLASS_NAME, "nameCard").text
        oldPrice = productCard.find_element(By.CLASS_NAME, "oldPriceCard").text
        currentPrice = productCard.find_element(
            By.CLASS_NAME, "priceCard").text

        productData = {"name": name, "active_sale": True if oldPrice else False, "old_price": oldPrice if oldPrice else None,
                       "price": currentPrice, "url": url, "date": datetime.today().strftime('%Y-%m-%d')}

        pageData.append(productData)

    return pageData


def navigateToNextPage():
    nextButton = driver.find_element(By.CLASS_NAME, "nextLink")
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", nextButton)
    time.sleep(0.5)
    nextButton.click()


options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get("https://www.kabum.com.br/hardware")

title = driver.title

consentButton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
consentButton.click()
data = []
pageData = extractData()
data.extend(pageData)
print(data)


wait = WebDriverWait(driver, timeout=100)

navigateToNextPage()

WebDriverWait(driver, 30).until(EC.url_changes(driver.current_url))
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "productCard"))
)


driver.quit()
