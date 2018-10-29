import time
from selenium import webdriver
import wget


def selenium_utils():
    browser = webdriver.Chrome('../driver/chromedriver')  # chromium driver path for web driver initialization
    cv_url = r"https://voice.mozilla.org/tr/listen"  # mozilla common voice url

    browser.get(cv_url)
    browser.implicitly_wait(10)  # wait
    time.sleep(2)

    while True:
        try:
            play_element = browser.find_elements_by_xpath(
                "//div[contains(@class, 'primary-button') and contains(@class, 'play')]"
            )
            # Return "primary-class"'s elements. checks for elements whether is play button.
            for x in range(len(play_element)):
                value = 0
                # check play button state from elements innerHTML
                if "play" in play_element[x].get_attribute('innerHTML'):
                    print("playback starting")
                    play_element[x].click()

                    # fetch audio url and download
                    audio_url = browser.find_element_by_xpath(
                        "//div[@id='root']//audio"
                    ).get_attribute("src")
                    wget.download(audio_url, "../data/" + str(value).zfill(2) + ".mp3")
                    value += 1

                    transcript_xPath_list = []

                    for index in range(1,5,1):
                        value = 0
                        transcript_xPath_generic ='//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div['+str(index)+']/div'
                        print(index)
                        transcript_xPath_list.append(transcript_xPath_generic)

                        # fetch text
                        element = browser.find_element_by_xpath(
                            transcript_xPath_list[value]

                        ).get_attribute("innerHTML")
                        print(element)
                        value += 1



                # if state is stop then wait for playback ends.
                elif "stop" in play_element[x].get_attribute('innerHTML'):  # Ara kontrol
                    print("wait")
                    time.sleep(5)

                if "play" in play_element[x].get_attribute('innerHTML'):
                    vote_yes_element = browser.find_element_by_xpath(
                        " //button[@class='Vote-Button.yes']"
                    )
                    vote_yes_element.click()
                    print(vote_yes_element.get_attribute("innerHTML"))
                    exit(-1)

        except Exception as ex:
            print(ex)


selenium_utils()
browser.close()
