import socket

HOST = '127.0.0.1'
PORT = 9999

# 웹서버: 80, ftp: 21... --> well known port number
# 0 ~ 1024: 표준 통신 프로토콜

# 주소 체계(address family): IPv4, 소켓타입:TCP
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 디폴트 값이다 인자없이 만들어도됨
server_socket = socket.socket()
# 이미 열린 포트 충돌시 재사용 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()
# accept 함수에서 대기, 클라이언트 접속 시 새로운 소켓을 리턴
client_socket, addr = server_socket.accept() 

# 접속한 클라이언트의 주소 출력
print('Connected by', addr)

while True:
    #메세지 수신대기
    data=client_socket.recv(1024)
    if not data:
        break
    # data(byte array)를 문자열로 변환하여 출력
    print('Received from',addr,data.decode())

    # 받은 문자열을 다시 클라이언트로 전송(에코)
    client_socket.sendall(data)

client_socket.close()
server_socket.close()
