from threading import Thread
import requests
import time


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), resp.text)


t1 = Thread(target=getHtml, args=('http://naver.com',))  # 1초
t1.start()
t2 = Thread(target=getHtml, args=('https://www.daum.net',)) # 2초 스레드를 나눠서 쓰면 2초걸린다.
t2.start()


# 스레드를 안쓰는 경우
# getHtml('https://www.daum.net')  # 1초 1개를 같이써서 시간이 3초걸린다.
# getHtml('https://naver.com')    # 2초
