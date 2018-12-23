import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
url = 'https://www.youtube.com/channel/UCFdTiwvDjyc62DBWrlYDtlQ/videos?sort=p&view=0&flow=grid'
resp = requests.get(url,headers=headers)
soup = BeautifulSoup(resp.text, 'lxml')

target=soup.find_all('a')
txt = open('video-title.txt', 'w', encoding = 'UTF-8')
for i in target:
	f=i.get_text().strip()
	txt.write(f)
txt.close()


