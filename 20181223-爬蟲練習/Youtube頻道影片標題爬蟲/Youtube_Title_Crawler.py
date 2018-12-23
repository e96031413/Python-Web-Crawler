import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
url = 'https://www.youtube.com/channel/UCFdTiwvDjyc62DBWrlYDtlQ/videos'
resp = requests.get(url,headers=headers)
soup = BeautifulSoup(resp.text, 'lxml')

target=soup.find_all('a')
for i in target:
	print(i.get_text().strip())