import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True  # Enable headless mode
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.get("https://courses.students.ubc.ca/browse-courses")

# Navigate to table of courses
body = driver.find_element(By.TAG_NAME, "body")
dialog = body.find_element(By.CLASS_NAME, "dialog-off-canvas-main-canvas")
page = dialog.find_element(By.CLASS_NAME, "l-page")
main = page.find_element(By.ID, "main-content")
content = main.find_element(By.CLASS_NAME, "l-page__content")
div = content.find_element(By.TAG_NAME, "div")
node = div.find_element(By.CLASS_NAME, "l-node")
node_content = node.find_element(By.CLASS_NAME, "l-node__content")
section = node_content.find_element(By.ID, "block-reactsubjectstable")
subjects = section.find_element(By.ID, "subjects-table")
div_two = subjects.find_element(By.TAG_NAME, "div")
muibox = div_two.find_element(By.TAG_NAME, "div")
muibox_two = WebDriverWait(muibox, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='subjects-table']/div/div/div[2]")))

printing = muibox_two.get_attribute("class")

print(printing)

driver.quit()

