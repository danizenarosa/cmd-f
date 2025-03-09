import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True  # Enable headless mode
options.add_argument("--headless")

driver = webdriver.Chrome(options = options)

driver.get("https://courses.students.ubc.ca/browse-courses")

# Navigate to table of courses
try:

    table = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div/div/div/div[3]/section/div/div/div/div[2]/div[2]/table/tbody")))

    printing = table.get_attribute("class")

    print(printing)

    rows = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "tr")))

    for x in rows:
        tdprint = x.get_attribute("id")
        print(tdprint)
        

finally:
    driver.quit()

