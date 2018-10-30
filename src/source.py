import time
from selenium import webdriver
import wget


def selenium_utils():
    browser = webdriver.Chrome('../driver/chromedriver')  # chromium driver path for web driver initialization
    cv_url = r"https://voice.mozilla.org/tr/listen"  # mozilla common voice url


    browser.get(cv_url)
    browser.implicitly_wait(10)  # wait
    time.sleep(2)


    audioCount = 0
    indexForTranscriptList = 0
    generic_variable = 1
    transcript_list = []

    while True:
        try:
            time.sleep(5)
            play_element = browser.find_element_by_xpath(
                "//div[contains(@class, 'primary-button') and contains(@class, 'play')]"
            )

            # check play button state from elements innerHTML
            if "play" in play_element.get_attribute('innerHTML'):
                print("playback starting")
                play_element.click()
            # if state is stop then wait for playback ends.
            while "play" not in play_element.get_attribute("innerHTML"):
                print("Stop Button Active")
                time.sleep(0.5)
            print(generic_variable)
            # Create generic automated xPath string
            transcript_xPath_generic = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[' \
                                       + str(generic_variable) + \
                                       ']/div'
            # fetch text
            element = browser.find_element_by_xpath(
                transcript_xPath_generic
            )
            generic_variable += 1
            # add text to trancript_list
            transcript_list.append(element.get_attribute("innerHTML"))
            # fetch audio url and download
            audio_url = browser.find_element_by_xpath(
                "//div[@id='root']//audio"
            ).get_attribute("src")
            wget.download(audio_url, "../data/" + str(audioCount).zfill(2) + ".mp3")
            audioCount += 1

            #grep Yes vote button and click it.
            button_yes = browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div[2]/div/div[4]/button[1]'
            )
            button_yes.click()


            print("Transcript :" + transcript_list[indexForTranscriptList])
            print("Audio Url : " + audio_url)

            if generic_variable > 5:
                indexForTranscriptList = 0
                generic_variable = 1
                if "contribution" in browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div').get_attribute("innerHTML"):
                    retryButton = browser.find_element_by_xpath(
                        '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/button'
                    )
                    retryButton.click()
                    del transcript_list[:]
                    continue


            indexForTranscriptList += 1
        except Exception as ex:
          print(ex)

selenium_utils()

