import json
from _thread import *
import socket

HOST = '127.0.0.1'
PORT = 6000
FILE_PATH = 'C:/Temp/received/data'


def receive_thread(client_socket, addr):
    try:
        # 파일 크기 수신
        # size = client_socket.recv(1024)
        # size = int(size.decode())
        # print('수신할 파일 크기: ', size)

        # json 문자열을 수신
        finfo = client_socket.recv(1024).decode()
        finfo = json.loads(finfo)
        print(f"파일명: {finfo.get('file_name')}, 파일크기: {finfo.get('file_size')}")
        size = finfo.get('file_size')
        fpath = 'c:/temp/received/'+finfo.get('file_name')

        # 준비상태 전송
        client_socket.send('ready'.encode())

        # 파일 수신
        total_size = 0
        with open(fpath, 'wb') as f:
            while True:
                data = client_socket.recv(1024)
                f.write(data)
                total_size += len(data)
                if total_size >= size:
                    break

            print(f'수신 완료: {total_size} bytes')
    except Exception as e:
        print(e)
    finally:
        client_socket.close()


with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            client_socket, addr = s.accept()  # 접속 대기
            # 스레드 가동
            start_new_thread(receive_thread, (client_socket, addr))

    except Exception as e:
        print(e)
