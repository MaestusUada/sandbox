import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import urlretrieve

def driver_initialization():

    browser = webdriver.Chrome('../driver/chromedriver') #chromium driver path for web driver initialization
    cv_url = r"https://voice.mozilla.org/tr/listen" # mozilla common voice url

    browser.get(cv_url)
    browser.implicitly_wait(10) #wait
    time.sleep(2)

    while True:
        try:





            #Return "primary-class"'s elements. checks for elements whether is play button.
            for x in range(len(element)):
                if "play" in element[x].get_attribute('innerHTML'):
                    print("playback starting")
                    element[x].click()
                    audio_url = browser.find_element_by_xpath("//div[@id='root']//audio").get_attribute("src")

                elif "stop" in element[x].get_attribute('innerHTML'): #Ara kontrol
                    print("wait")
                    time.sleep(5)

        except Exception as ex:
            print(ex)

driver_initialization()
browser.close()
