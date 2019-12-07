#! /usr/bin/python
from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#browser = webdriver.Firefox()

mv=[]
year=[]

mf = open('movie_name.txt', 'r')
yf = open('movie_year.txt', 'r')

for line in mf:
    mv += [line[:-1]]
	
for line in yf:
    year += [line[:-1]]
	
#print(year[333])
#print(mv[333])
	
print(mv[0])	
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

browser = webdriver.Firefox(firefox_binary=binary)
time.sleep(4)
#reader = open("list_genre.txt", "r")


for i in range(0,120):
	movie = mv[i]
	yr= year[i]

	url = 'https://www.google.com/trends/explore?cat=3&date='+yr+'-01-01%20'+yr+'-12-31&q=The%20Shawshank%20Redemption,'+movie	#Narendra Modi'
	browser.get(url)
	print ("browser opened")
	time.sleep(8)
	optionButton = browser.find_element_by_css_selector('div.widget-container:nth-child(2) > trends-widget:nth-child(2) > ng-include:nth-child(1) > widget:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > widget-actions:nth-child(2) > button:nth-child(1)')
	csvButton = browser.find_element_by_css_selector('div.widget-container:nth-child(2) > trends-widget:nth-child(2) > ng-include:nth-child(1) > widget:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > widget-actions:nth-child(2) > div:nth-child(2) > button:nth-child(3)')
	optionButton.click()
	time.sleep(2)
	csvButton.click()
	time.sleep(10)
	# time.sleep(5)
	# url = 'https://www.google.com/trends/explore?q=Taylor Swift'
	# browser.get(url)
	# time.sleep(4)
	# optionButton = browser.find_element_by_css_selector('.fe-line-chart-header-container > widget-actions:nth-child(2) > button:nth-child(1)')
	# csvButton = browser.find_element_by_css_selector('.fe-line-chart-header-container > widget-actions:nth-child(2) > div:nth-child(2) > button:nth-child(3)')
	# optionButton.click()
	# time.sleep(2)
	# csvButton.click()


"""
div.widget-container:nth-child(2) > trends-widget:nth-child(2) > ng-include:nth-child(1) > widget:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > widget-actions:nth-child(2) > div:nth-child(2) > button:nth-child(3)

div.widget-container:nth-child(2) > trends-widget:nth-child(2) > ng-include:nth-child(1) > widget:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > widget-actions:nth-child(2) > button:nth-child(1)


.fe-line-chart-header-container > widget-actions:nth-child(2) > button:nth-child(1)

.fe-line-chart-header-container > widget-actions:nth-child(2) > div:nth-child(2) > button:nth-child(3)
.fe-line-chart-header-container > widget-actions:nth-child(2) > div:nth-child(2)
.fe-line-chart-header-container > widget-actions:nth-child(2)
.fe-line-chart-header-container
.fe-line-chart

widget-actions.ng-scope > button:nth-child(1)
widget-actions.ng-scope
.fe-geo-chart-generated > div:nth-child(1)
.fe-geo-chart-generated
.fe-geo-chart-generated
div.widget-container:nth-child(2) > trends-widget:nth-child(2) > ng-include:nth-child(1) > widget:nth-child(1) > div:nth-child(1)
div.widget-container:nth-child(2) > trends-widget:nth-child(2) > ng-include:nth-child(1) > widget:nth-child(1)

div.widget-container:nth-child(2) > trends-widget:nth-child(2)
.widget-container-wrapper
div.widget-container:nth-child(2)
.explorepage-content > div:nth-child(1)
div.widget-container:nth-child(2) > trends-widget:nth-child(2) > ng-include:nth-child(1) > widget:nth-child(1) > div:nth-child(1) > .fe-geo-chart-generated > widget-actions.ng-scopes  > button:nth-child(1)
.fe-geo-chart-generated
.fe-line-chart-header-container
.fe-line-chart
div.widget-container:nth-child(1) > trends-widget:nth-child(2) > ng-include:nth-child(1) > widget:nth-child(1) > div:nth-child(1)
"""