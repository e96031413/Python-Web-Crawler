from selenium import webdriver
import time
url=input('請輸入網址:')

browser = webdriver.Firefox()
browser.set_window_size(1200,4500)
browser.get(url) # Load page
browser.save_screenshot('books.png')
browser.close()
