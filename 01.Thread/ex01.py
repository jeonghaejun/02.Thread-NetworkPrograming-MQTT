# import threading  # 모듈을 찾을 때 워킹디렉토리 먼저 찾아서 파일명이랑 같으면 오류난다.
from threading import Thread

count = 2  # 운영할 스레드의 개수


def sum(low, high):
    global count
    total = 0
    for i in range(low, high):
        total += i
    print('Subthread', total)
    count -= 1


# t = threading.Thread(target=sum, args=(1, 100000))
t1 = Thread(target=sum, args=(1, 100000))
t2 = Thread(target=sum, args=(100, 10000000))
t1.start()
t2.start()

while count != 0:  # 작업스레드가 다 종료되고 메인스레드가 시작된다.
    pass

print('Main Thread')
