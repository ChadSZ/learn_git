IP 地址···

#### requests 命令

* 网络爬虫的应用

* python 下载豆瓣

* 安装 requests
pip install requests

http 请求库

## 多线程、多进程、协程

同步：程序一步一步的执行下去

多进程：执行一个程序就是开启了一个进程，不能直接通信，占用资源较多。

多线程：进场开启多个线程，线程可以通信，占用资源少。

协程(Coroutine)：单线程调度 gevent


### IDM 下载

## 任务

1. 使用pymysql 连接 之前练习的数据库，完成以下步骤 CURD

1. 首先，要导入cursors库，
2. 加入连接
3. 使用cursors游标

* 在你新建的表格中增加一条记录

* 查询记录

[帮助链接](https://pymysql.readthedocs.io/en/latest/user/examples.html)

2. 多线程TCP服务器+100个tcp客户端并发访问 / 多线程(100)Http请求程序 flask web

* 遇到小问题：socket 错误之：OSError: [WinError 10057] 由于套接字没有连接并且(当使用一个 sendto 调用发送数据报套接字时)没有提供地址，发送或接收数据的请求没有被接受。...

* 原因是没有套接字没有连接地址： tcp_socket.connect(address)