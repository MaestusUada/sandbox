import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("../driver/chromedriver")


def driverInitialization():
    browser.get("https://voice.mozilla.org/tr/listen")
    browser.implicitly_wait(10)

    while True:
        try:

            element = browser.find_element_by_xpath(
                "//div[contains(@class, 'primary-button') and contains(@class, 'play')]")
            element.click()
            print("playback started.")
            stop_elem = browser.find_element_by_xpath(
                "//div[contains(@class, 'primary-button') and contains(@class, 'stop')]"
            )

            if stop_elem is not None:
                if "stop" not in stop_elem.get_attribute("innerHTML"):
                    #BURAYA EVET BUTONU TIKLAMASI GELECEK
                else:
                    continue



        except Exception as ex:
            print(ex)
    time.sleep(2)

driverInitialization()
browser.close()
