from selenium import webdriver
from selenium.webdriver.chrome.service import Service as sv
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=sv(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get('https://www.library.chiyoda.tokyo.jp/')

e1 = driver.find_elements_by_class_name('schedule-list01__status')

print([s.text for s in e1])