from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
dates_xpath = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time'

driver.get("https://www.python.org/")
dates = driver.find_elements(by=By.XPATH, value=dates_xpath)
events = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

upcoming_events = {}

for i in range(len(dates)):
    upcoming_events[i] = {
        'time': dates[i].text,
        'name': events[i].text,
    }

print(upcoming_events)
