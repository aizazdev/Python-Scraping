from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome(executable_path="C:\Program Files (x86)\Chromedriver\chromedriver.exe")
driver.get("https://directory.ntschools.net/#/schools")
selector = driver.find_elements_by_css_selector('#search-panel-container .nav-link') 
elements = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
    )

for e in elements:
    print(e.text)

driver.quit()