import socket

# 클라이언트 설정
HOST = '192.168.118.137'  # 라즈베리 파이의 IP 주소
PORT = 12347  # 서버와 동일한 포트 번호

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("전송할 명령 입력: ")
    client_socket.send(message.encode())

client_socket.close()