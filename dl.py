#The selenium.webdriver module provides all the WebDriver implementations. Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote. The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Instance of Firefox WebDriver is created.
options = webdriver.FirefoxOptions()
options.headless=True
driver = webdriver.Firefox(options=options)

#The driver.get method will navigate to a page given by the URL. WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control to your test or script. It’s worth noting that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded.:
driver.get("https://www.codechef.com/MARCH19B")

img = driver.find_element_by_tag_name("body").screenshot("ho.png")

print(driver.title)
tbody = driver.find_element_by_tag_name("tbody")
#print("Found:", len(tbody))
#tr = tbody[0].find_elements_by_tag_name("tr")
#td = tr[0].find_element_by_id("cc-problem-name")

tdlst = tbody.find_elements_by_tag_name("tr")
l = len(tdlst)

for i in range(0, l):
  td = tdlst[i].find_element_by_xpath("td/div/span/a")

  ques = td.get_attribute("href")
  print(ques)

#print(tbody)

#print(tr[0])
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source

driver.close()


