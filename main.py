from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random


def login(username, password):
    browser = webdriver.Chrome()

    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        while True:
            browser.get("https://www.instagram.com/explore/people/")
            time.sleep(random.randrange(180,240))
            for i in range(1,20):
                try:
                    follow_action = browser.find_element_by_xpath(f"/html/body/div[1]/section/main/div/div[2]/div/div/div[{i}]/div[3]/button").click()
                    print("Подписка оформлена")
                    time.sleep(random.randrange(180,240))    
                except:
                    pass


        browser.close()
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


login(username, password)