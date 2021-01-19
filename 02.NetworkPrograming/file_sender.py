import json
import os
import socket

# json(JavaScripot Object Notation)

HOST = '127.0.0.1'
PORT = 6000
FILE_PATH = 'C:/Users/wjdgo/iot_workspace/02.Thread,NetworkPrograming,MQTT/02.NetworkPrograming/ShopDB.sql'


def file_read(file_path):
    with open(file_path, 'rb')as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            yield data


def file_info(fpath):
    # file_name = fpath.split('/')[-1]
    # file_size = os.path.getsize(fpath)
    file_name = os.path.split(fpath)[1]
    file_size = os.path.getsize(fpath)


    return {
        'file_name': file_name,
        'file_size': file_size
    }


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        fileSize = os.path.getsize(FILE_PATH)

        finfo = file_info(FILE_PATH)
        # 파일 크기 전송
        print('전송 파일명', finfo.get('file_name'))
        print('전송 파일 크기', finfo.get('file_size'))
        msg = json.dumps(finfo)   # <--- 제이슨으로 만들어지는 자료에는 개행문자는 안들어간다.
        s.sendall(msg.encode())

        # 준비 상태 수신
        isready = s.recv(1024).decode()
        if isready == 'ready':
            # 파일전송
            for data in file_read(FILE_PATH):
                s.sendall(data)
            print('전송완료')

    except Exception as e:
        print(e)
