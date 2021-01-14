import socket

HOST = '127.0.0.1'
PORT = 9999

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 디폴트 값이다 인자없이 만들어도됨
client_socket = socket.socket()
# 서버와 연결
client_socket.connect((HOST, PORT))

# 메세지 전송
client_socket.sendall('안녕'.encode())

# 메세지 수진
data = client_socket.recv(1024)
print('Received', data.decode())

client_socket.close()
