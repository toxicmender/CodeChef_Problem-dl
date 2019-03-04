#The selenium.webdriver module provides all the WebDriver implementations. Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote. The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Instance of Firefox WebDriver is created.
options = webdriver.FirefoxOptions()
options.headless=True
driver = webdriver.Firefox(options=options)

#The driver.get method will navigate to a page given by the URL. WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control to your test or script. It’s worth noting that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded.:
#driver.get("https://www.codechef.com/MARCH19B")

driver.get("https://www.codechef.com/MARCH19B/problems/CHNUM")

img = driver.find_element_by_id("problem-statement").screenshot("scr.png")

