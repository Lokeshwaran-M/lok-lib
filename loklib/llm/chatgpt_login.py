import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def click_login_button(driver):
    driver.find_element(
        By.CSS_SELECTOR, 'button[class="btn relative btn-primary"]').click()


def bypassing_cloudflare(driver):
    # Wait for CloudFlare challenge-form to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "challenge-form")))
    time.sleep(random.uniform(10, 15))
    driver.find_element(By.ID, "challenge-form").click()
    time.sleep(4)


def login_openai(driver, email_address, password):
    time.sleep(4)
    # type email_address
    driver.find_element(
        By.CSS_SELECTOR, 'input[name="username"]').send_keys(email_address)

    time.sleep(4)
    # click continue button
    driver.find_element(By.CSS_SELECTOR, 'button[name="action"]').click()

    time.sleep(4)
    # type user password
    driver.find_element(
        By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)

    # click continue button
    continue_button = driver.find_element(
        By.CSS_SELECTOR, 'button[name="action"]')
    time.sleep(4)
    continue_button.click()


def login_google_account(driver, password, email_address):
    # click the login button
    driver.find_element(
        By.CSS_SELECTOR, "button[data-provider='google']").click()

    # type email address
    driver.find_element(
        By.CSS_SELECTOR, "input[type='email']").send_keys(email_address)

    time.sleep(random.uniform(1, 3))

    # click next button
    driver.find_elements(By.CSS_SELECTOR, "button[type='button']")[3].click()

    # type password
    driver.find_element(
        By.CSS_SELECTOR, "input[type='password']").send_keys(password)

    # click next button
    driver.find_elements(By.CSS_SELECTOR, "button[type='button']")[3].click()


def skip_start_message(driver):
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "button.btn-neutral").click()
    time.sleep(3)
    driver.find_elements(By.CSS_SELECTOR, "button.btn-neutral")[1].click()
    time.sleep(3)
    driver.find_elements(By.CSS_SELECTOR, "button.btn-primary")[1].click()
