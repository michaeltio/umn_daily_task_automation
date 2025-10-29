import os
import csv
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

load_dotenv()
logging.info("Script Started")

data_file = "data.csv"
logging.info(f"Using data file: {data_file}")

data = []
try:
    with open(data_file, "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
except FileNotFoundError:
    logging.error(f"ERROR: File '{data_file}' not found.")
    logging.error("Please create data.csv in the same directory.")
    input("Tekan Enter untuk keluar...")
    exit()
except Exception as e:
    logging.error(f"Failed to read {data_file}: {e}")
    input("Tekan Enter untuk keluar...")
    exit()


logging.info("Data Loaded:")
for item in data:
    logging.info(item)

logging.info("Launching WebDriver...")
driver = webdriver.Chrome()

logging.info("Navigating to the website...")
driver.get("https://prostep.umn.ac.id/web/")

wait = WebDriverWait(driver, 10)
login_dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log in')]"))
)
login_dropdown.click()

login_umn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]//a[contains(text(), 'Log In for UMN')]"))
)
login_umn.click()

username_field = wait.until(
    EC.presence_of_element_located((By.ID, "username")))
password_field = wait.until(
    EC.presence_of_element_located((By.ID, "password")))

username_field.send_keys(os.getenv("STUDENT_EMAIL"))
password_field.send_keys(os.getenv("STUDENT_PASSWORD"))

login_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='submit' and @value='LOGIN']"))
)
login_button.click()

daily_task_link = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href, 'daily-task') and span[text()='Daily Task']]"))
)
daily_task_link.click()

for item in data:
    logging.info(f"Filling task for date: {item['date']}")

    wait.until(EC.presence_of_element_located((By.ID, "w1")))
    input_task_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(), 'Input New Task')]"))
    )
    input_task_button.click()

    date_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "taskdaily-task_date"))
    )
    date_field.send_keys(str(item['date']))

    start_time_field = driver.find_element(By.ID, "taskdaily-start_time")
    end_time_field = driver.find_element(By.ID, "taskdaily-end_time")

    start_time_field.clear()
    start_time_field.send_keys(str(item["start_time"]))
    end_time_field.clear()
    end_time_field.send_keys(str(item["end_time"]))

    descr_field = driver.find_element(By.ID, "taskdaily-descr")
    descr_field.clear()
    descr_field.send_keys(str(item["task_description"]))

    approver_dropdown = wait.until(
        EC.element_to_be_clickable((By.ID, "select2-type-container"))
    )
    approver_dropdown.click()

    approver_type = str(item.get("approver", "Supervisor")
                        ).strip().capitalize()
    if approver_type not in ["Supervisor", "Advisor"]:
        approver_type = "Supervisor"

    approver_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(text(), '{approver_type}')]"))
    )
    approver_option.click()
    logging.info(f"Selected Approver: {approver_type}")

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Submit')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    yes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", yes_button)
    driver.execute_script("arguments[0].click();", yes_button)

    logging.info("Form submitted successfully")

logging.info("All tasks have been filled.")
input("Tekan Enter untuk menutup browser...")
driver.quit()
