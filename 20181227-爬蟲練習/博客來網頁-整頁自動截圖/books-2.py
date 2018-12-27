from selenium import webdriver
import time
url='https://search.books.com.tw/search/query/cat/1/key/python/qsub/001/sort/5'
browser = webdriver.Firefox()
browser.get(url)
browser.set_window_size(1200,4500)
browser.get(url) # Load page
browser.save_screenshot('books.png')
browser.close()
