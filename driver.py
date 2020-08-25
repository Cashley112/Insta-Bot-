from time import sleep
from selenium import webdriver
from page_object_classes import LoginPage


browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = LoginPage(browser)
home_page.login("dolan_pettit","Richmond96")

browser.close()
