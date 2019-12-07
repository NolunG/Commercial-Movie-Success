#! /usr/bin/python
from selenium import webdriver
import time
browser = webdriver.Firefox()
url = 'https://www.google.com/trends/explore?q=Narendra Modi'
browser.get(url)

print ("browser opened")
time.sleep(4)
optionButton = browser.find_element_by_css_selector('.fe-line-chart-header-container > widget-actions:nth-child(2) > button:nth-child(1)')
csvButton = browser.find_element_by_css_selector('.fe-line-chart-header-container > widget-actions:nth-child(2) > div:nth-child(2) > button:nth-child(3)')
optionButton.click()
time.sleep(2)
csvButton.click()
time.sleep(5)
url = 'https://www.google.com/trends/explore?q=Taylor Swift'
browser.get(url)
time.sleep(4)
optionButton = browser.find_element_by_css_selector('.fe-line-chart-header-container > widget-actions:nth-child(2) > button:nth-child(1)')
csvButton = browser.find_element_by_css_selector('.fe-line-chart-header-container > widget-actions:nth-child(2) > div:nth-child(2) > button:nth-child(3)')
optionButton.click()
time.sleep(2)
csvButton.click()


