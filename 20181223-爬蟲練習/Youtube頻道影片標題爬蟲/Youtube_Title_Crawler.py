import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
url = 'https://www.youtube.com/channel/UCFdTiwvDjyc62DBWrlYDtlQ/videos?sort=p&view=0&flow=grid'
resp = requests.get(url,headers=headers)
soup = BeautifulSoup(resp.text, 'lxml')

target=soup.find_all('a')

#存成txt檔案
txt = open('video-title.txt', 'w', encoding = 'UTF-8')
for i in target:
	f=i.get_text().strip() #取得文字、去除左右的空格
	txt.write(f)           #寫入文字
	txt.write('\n') 	   #換行
txt.close()                #關閉檔案

