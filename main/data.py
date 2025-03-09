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

def navigate_section():
    body = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[3]")))
    divs = WebDriverWait(body, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "course-sections-box")))

    for index, div in enumerate(divs, start=1):
        section = WebDriverWait(div, 5).until(EC.visibility_of_element_located(
            (By.XPATH, f"/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[3]/div[{index}]/div/div[1]/div/div[1]/div/div[2]/p/a")
        ))
        text = section.text
        print(text)
        term = WebDriverWait(div, 5).until(EC.visibility_of_element_located(
            (By.XPATH, f"/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[3]/div[{index}]/div/div[2]/div/div[1]/div/div[2]/p")
        ))
        text = term.text
        print(text)
        activity = WebDriverWait(div, 5).until(EC.visibility_of_element_located(
            (By.XPATH, f"/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[3]/div[{index}]/div/div[2]/div/div[2]/div/div[2]/p")
        ))
        text = activity.text
        print(text)
        try:
            start_time = WebDriverWait(div, 5).until(EC.visibility_of_element_located(
                (By.XPATH, f"/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[3]/div[{index}]/div/div[3]/div/div[2]/div/div[2]/p")
            ))
            text = start_time.text
            print(text)
        except Exception as e:
            text = "None"
            print(text)
        try:
            end_time = WebDriverWait(div, 5).until(EC.visibility_of_element_located(
                (By.XPATH, f"/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[3]/div[{index}]/div/div[4]/div/div[2]/div/div[2]/p")
            ))
            text = end_time.text
            print(text)
        except Exception as e:
            text = "None"
            print(text)
        try:
            days = WebDriverWait(div, 5).until(EC.visibility_of_element_located(
                (By.XPATH, f"/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[3]/div[{index}]/div/div[3]/div/div[3]/div/div[2]/p")
            ))
            text = days.text
            print(text)
        except Exception as e:
            text = "None"
            print(text)
        

    driver.back()

def navigate_course():

    try:
        tbody = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[2]/div/div[2]/table/tbody")))
        rows = WebDriverWait(tbody, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "tr")))
    except Exception as e:
        driver.back()
        return

    for index, row in enumerate(rows, start=1):
        a = WebDriverWait(row, 5).until(EC.visibility_of_element_located(
            (By.XPATH, f"/html/body/div[2]/div/main/div/div/div/div[2]/section/div/div/div/div[2]/div/div[2]/table/tbody/tr[{index}]/td[1]/div[2]/a")
        ))
        a.click()
        navigate_section()

    driver.back()

def navigate_page():
    tbody = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div/div/div/div[3]/section/div/div/div/div[2]/div[2]/table/tbody")))
    rows = WebDriverWait(tbody, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "tr")))

    for index, row in enumerate(rows, start=1):
        a = WebDriverWait(row, 5).until(EC.visibility_of_element_located(
            (By.XPATH, f"/html/body/div[2]/div/main/div/div/div/div[3]/section/div/div/div/div[2]/div[2]/table/tbody/tr[{index}]/td[1]/div[2]/a")
        ))
        a.click()
        navigate_course() 

# Start navigating and scraping data
try:
    navigate_page()
    while True:
        next_page_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[2]/div/main/div/div/div/div[3]/section/div/div/div/div[2]/table/tfoot/tr/td/div/div/div/div[2]/button[2]")
        ))

        if next_page_button.is_enabled():
            next_page_button.click()
            navigate_page()
        else:
            print("No more pages available.")
            break

finally:
    driver.quit()
