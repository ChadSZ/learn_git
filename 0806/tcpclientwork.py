import socket

tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

address = ("127.0.0.1",7120)

tcp_sock.connect(address)

bytes_str = input("请您准备输入字节：")
# print(type(bytes_str))

# 字符转为字节
b1 = bytes(bytes_str,encoding='utf-8')

tcp_sock.send(b1)
# tcp_sock.send(b"p_aabc")
# print(type(b"aaa"))
data = tcp_sock.recv(1024)
print(f"接收到的数据是：{data}")

tcp_sock.close()