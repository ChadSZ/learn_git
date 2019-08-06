import socket

num = 0
bytes_num = 0

#
udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

address = ("0.0.0.0",7010)
udp_sock.bind(address)
print(f"{address}地址绑定成功！")

# 
while True:
    data,client_addr = udp_sock.recvfrom(1024)
    num = num + 1
    bytes_num = bytes_num + len(data)
    print(f"从{client_addr}第{num}接收到字节数为{bytes_num}的数据：{data}")

    udp_sock.sendto(data,client_addr)

    # udp_sock.close()