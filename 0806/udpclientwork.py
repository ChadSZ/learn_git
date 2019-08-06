import socket

udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

address = ("127.0.0.1",7010)

# 绑定地址，并发送数据
# udp_sock.sendto(b"hello world!",address)

input_str = input("请输入字节数据：")
input_bytes = bytes(input_str,encoding = "utf-8")

udp_sock.sendto(input_bytes,address)

data = udp_sock.recv(1024)
print(f"接收到的数据是：{data}")

udp_sock.close()