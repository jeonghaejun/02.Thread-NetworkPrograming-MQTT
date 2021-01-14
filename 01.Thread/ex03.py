from threading import Thread
import requests
import time


def getHtml(url):
    resp = requests.get(url)
    with open('./image.jpg', 'wb') as f:
        f.write(resp.content)


url = 'https://ssl.pstatic.net/mimgnews/image/005/2021/01/08/611811110015405754_4_20210108112002123.jpg?type=w540'

url_list = []

for url in url_list:  # url하나당 스레드 하나씩해서 다운로드
    t1 = Thread(target=getHtml, args=(url,))
    t1.start()
