from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from data import text as WELCOME_MSG
DEFAULT_WAIT_TIME = 3

def sleep(seconds = None):
    seconds = seconds or DEFAULT_WAIT_TIME
    time.sleep(seconds)

def init():
    options = Options()
    options.add_argument("--user-data-dir=/home/qitpy/.config/google-chrome")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.free4talk.com/room/Ic739")

    sleep()
    # click on the avatar of screen
    element = driver.find_element(By.XPATH, "//div[@id='root']//div//div//div[2]//button//div")
    element.click()

    sleep()
    element = driver.find_element(By.XPATH, "//div[@role='tab']")
    element.click()

    return driver

def send_text(driver, text):
    if not text:
        return

    text_area = driver.find_element(By.XPATH, "//textarea")
    text_area.click()

    lines = text.split('\n')
    actions = ActionChains(driver)
    for line in lines:
        actions.send_keys(line)
        actions.key_down(Keys.SHIFT).send_keys(Keys.RETURN).key_up(Keys.SHIFT)
        sleep(0.2)
    actions.perform()

    sleep()
    element = driver.find_element(By.XPATH, "//div[@class='text-input']//button")
    element.send_keys(Keys.ENTER)


def start_loop():
    while True:
        text = input("Enter your message: ")
        if text:
            # read data from data.md
            with open('data.md', 'r') as file:
                lines = file.readlines()

            for line in lines:
                print(line)

            sleep()
            # send_text(msg)

def main():
    driver = init()
    # start_loop()
    # send_text()

if __name__ == '__main__':
    text = input("Enter your message: ")
    driver = init()
    sleep()
    if text:
        for msg in WELCOME_MSG:
            send_text(driver, msg)
            sleep()
    sleep(5)