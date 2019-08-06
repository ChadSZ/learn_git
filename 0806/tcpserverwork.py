import socket


num = 0

byte_num = 0

# 创建ipv4的tcp socket
tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定地址
address = ("0.0.0.0",7120)
tcp_sock.bind(address)

# 监听
tcp_sock.listen(10)

# 循环的方式来查询是否有数据接收
while True:
    # global num
    # 等待链接,如果有空闲，则返回新的套接字
    obj_conn,addr = tcp_sock.accept()
    data = obj_conn.recv(1024)

    # 判断接收到的字节是否为空，为空直接关闭
    if data == b"":
        obj_conn.close()
    else:
        # global num
        num = num+1    
        byte_num = len(data) + byte_num
    print(f"我累计接收了{num}次数据，总的字节数为{byte_num}，此次数据为{data}")
    
    #发送已接收到的数据
    obj_conn.send(data)
    obj_conn.close()