import os
import random
import time

import undetected_chromedriver as uc
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from .import chatgpt_login
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class ChatGPT:
    OPENAI_URL = "https://chat.openai.com/chat"

    def __init__(self,headless=True, wait=10):
        self.driver = self.set_driver(headless, wait)
        self.driver.get(ChatGPT.OPENAI_URL)
        self.login(self.driver)

    def set_driver(self, headless, wait_time):
       
        
        if headless:
            options = uc.ChromeOptions()
            options.add_argument("--headless")
            # options.add_argument('--no-sandbox')
            # options.add_argument('--disable-dev-shm-usage')
            driver = uc.Chrome(options=options)
        else :
            class OR_Chrome(uc.Chrome):
                def __del__(self):
                    pass
            driver = OR_Chrome()       
        driver.implicitly_wait(wait_time)
        return driver

    def set_chat_history_and_training(self, check):
        # Open Data Controls settings window
        self.driver.find_element(
            By.XPATH, '//div[@class="group relative" and @data-headlessui-state=""]').click()
        self.driver.find_element(
            By.XPATH, '//a[contains(text(),"Settings")]').click()
        self.driver.find_element(
            By.XPATH, '//button[contains(., "Data controls")]').click()

        checked_value = self.driver.find_element(
            By.XPATH, "//button[@aria-checked]").get_attribute("aria-checked")
        if checked_value != check:
            # click Chat History and Training Button
            self.driver.find_element(
                By.XPATH, '//button[contains(@id, "headlessui-switch-")]').click()

        # close settings window
        self.driver.find_element(
            By.XPATH, '//div[@class="sm:mt-0"]/button').click()

    def get_driver(self):
        return self.driver
    def get_driver_url(self):
        return self.driver.command_executor._url

    def login(self,driver):
        # login.bypassing_cloudflare(driver)
        chatgpt_login.click_login_button(driver)

        if load_dotenv(".env"):
            load_dotenv(".env")
        elif load_dotenv():
            load_dotenv()
        else:
            print(".env is not defined")
            
        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        PASSWORD = os.getenv("PASSWORD")
        chatgpt_login.login_openai(
            driver, email_address=EMAIL_ADDRESS, password=PASSWORD)
        chatgpt_login.skip_start_message(driver)

    def set_gpt_model(self, model):
        model_element_dic = {
            "GPT-3.5": "//span[contains(text(), 'Default (GPT-3.5)')]",
            "GPT-3.5-Legacy": "//span[contains(text(), 'Legacy (GPT-3.5)')]",
            "GPT-4": "//span[contains(text(), 'GPT-4')]",
        }
        self.driver.find_element(
            By.XPATH, '//div[@class="relative w-full md:w-1/2 lg:w-1/3 xl:w-1/4"]//button').click()
        self.driver.find_element(
            By.XPATH, model_element_dic.get(model)).click()

    def send_prompt(self, prompt):
        textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea")
        textarea.clear()
        textarea.send_keys(prompt)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button.absolute").click()

    def get_user_prompt(self):
        time.sleep(5)
        user_elements = self.driver.find_elements(
            By.XPATH,
            '//div[contains(@class, "group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 dark:bg-gray-800")]',
        )

        return [user_element.text for user_element in user_elements]

    def get_gpt_response(self):
        time.sleep(5)
        gpt_elements = self.driver.find_elements(
            By.XPATH,
            '//div[contains(@class, "group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]")]',
        )
        with open('res_chatgpt.md', 'w') as f:
            f.write(f"# pmt : {self.get_user_prompt()} \n")
            for res_id ,gpt_element in enumerate(gpt_elements):
                f.write(f"## res {res_id} : \n"+gpt_element.text + "\n\n")
        

        return [gpt_element.text for gpt_element in gpt_elements]

    def resume_chat(self, chatid):
        self.driver.get(ChatGPT.OPENAI_URL + f"/c/{chatid}")


def res(pmt):
    chatgpt = ChatGPT(headless=False, wait=10)
    chatgpt.send_prompt(pmt)
    time.sleep(5)
    res = chatgpt.get_gpt_response()
    return res[-1]



if __name__ == "__main__":
    new_chat = ChatGPT(headless=False, wait=10)
    # new_chat.set_gpt_model(model="GPT-3.5") # GPT-3.5, GPT-3.5-Legacy, GPT-4
    # new_chat.set_chat_history_and_training(check="False") # true or false

    while True:
        cmd = input("cmd : ")
        if cmd == "stop":
            break
        new_chat.send_prompt(prompt=cmd)
        print("jam : ", new_chat.get_gpt_response())
