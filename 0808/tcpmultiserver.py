import socket
import threading
from threading import Thread

def recv_msg(client_socket):
    while True:
        recv_data = client_socket.recv(1024)
        if recv_data:
            recv_content = recv_data.decode('gbk')
            print('>>',recv_content)
        else:
            print("客户端断开链接")
            client_socket.close()
            break

def send_msg(client_socket):
    while True:
        send_data = input("<<")
        send_content = send_data.decode('gbk')
        client_socket.send(send_content)
        

if __name__ == "__main__":

    tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 设置端口复用
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    address = ("0.0.0.0",7021)
    tcp_sock.bind(address)
    tcp_sock.listen(100)

    while True:
        # 等待链接
        conn,client_addr = tcp_sock.accept()
        print(f"{client_addr} connected!")
       
        client_thread_recv = threading.Thread(target=recv_msg,args=(conn,))

        client_thread_recv.setDaemon(True)

        client_thread_send = threading.Thread(target=send_msg,args=(conn,))

        client_thread_send.setDaemon(True)

        client_thread_recv.start()
        client_thread_send.start()
    
    tcp_sock.close()




