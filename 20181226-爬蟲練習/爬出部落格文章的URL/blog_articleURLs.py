import requests
import re
from bs4 import BeautifulSoup

url="https://www.cnblogs.com/tszr/archive/2018/12.html"

request=requests.get(url)
content=request.content
soup=BeautifulSoup(content,"html.parser")
target=soup.find_all(class_='entrylisttitle')
for link in target:
	print(link.get('href').strip())
