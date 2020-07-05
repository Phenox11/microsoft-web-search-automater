from config import info
import time
import logging
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import requests
import random

options = Options()
options.headless = True
Path = info.path
user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(executable_path=Path)
#driver.set_window_size(360,640)

wait = WebDriverWait(driver, 90)

def wait_until(string):
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'{string}')))

usernames = info.usernames

def main():
    r = requests.get('https://random-word-api.herokuapp.com//word?number=30')
    r = str(r.content).replace("\"", " ").replace(",", "").replace("b'[", "").replace(" ]'", "")
    r = r.split()
    print(r)

    try:
        driver.get('https://bing.com/')
        time.sleep(.5)
        wait_until('#id_s')
        driver.find_element_by_xpath('//*[@id="id_a"]').click()
        wait_until('#i0116')
        name = driver.find_element_by_css_selector('#i0116')
        name.send_keys(info.username, Keys.RETURN)
        wait_until('#i0118')
        password = driver.find_element_by_css_selector('#i0118')
        password.send_keys(info.password)
        time.sleep(.5)
        password.send_keys(Keys.RETURN)
        wait_until('#sb_form_q')
        search_bar = driver.find_element_by_css_selector('#sb_form_q')
        search_bar.send_keys(r[0])
        search_bar.send_keys(Keys.RETURN)
        time.sleep(1)
        for x in r:
            wait_until('#sb_form_q')
            search_bar = driver.find_element_by_css_selector('#sb_form_q')
            search_bar.send_keys(Keys.CONTROL, 'a')
            search_bar.send_keys(Keys.BACKSPACE)
            search_bar.send_keys(x)
            search_bar.send_keys(Keys.RETURN)
            time.sleep(.5)






        time.sleep(5)
        driver.quit()
    except Exception as e:
        logging.exception('issue')
        driver.quit()


if __name__ == "__main__":
    main()
