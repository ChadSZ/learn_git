import socket
from threading import Thread
flag= True
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

address = ("127.0.0.1",7021)

tcp_socket.connect(address)

def rece_msg(tcp_socket):
    global flag
    while flag:
        recv_msg = tcp_socket.recv(1024)
        if recv_msg == "exit":
            flag = False
        print('接收到的信息为：%s' % recv_msg)

def send_msg(tcp_socket):
    global flag
    while flag:
        send_msg = input('请输入要发送的内容')
        # bytes_in = bytes(send_msg,encoding="utf-8")
        bytes_in = send_msg.encode('utf-8')
        # tcp_socket.send(bytes(send_msg,encoding="utf-8"))
        for i in range(100):
            tcp_socket.send(bytes_in)
        if send_msg == "exit":
            flag = False
        
        data = tcp_socket.recv(1024)
        print(f"接收到的数据：{data}")


def main():
    while True:
        print('*'*50)      
        task = []
        t=Thread(target=send_msg, args=(tcp_socket,))
        task.append(t)
        t.start()

        for t in task:
            t.join()

if __name__ == '__main__':
    main()
