## python
### while 循环
    while condition:
        xxx(下一步操作)
        ...
* break:退出此层循环
* continue:跳过本次循环

* 任务：
1. 高斯求和 1+2+3+...100 = ？
2. 求1-100以内的奇数和

### for 循环
for element in ...(str、list、tuple、dict ...)
* 遍历字符串里面的每个字符
* 遍历列表中的每个元素
* 遍历元组中的每个元素(不可变的)
* 遍历字典中的每个元素
* 遍历集合中的每个元素(set)
* 遍历range中的每个元素

### range函数
生成指定范围的数组
range(100) 
* 默认生成的是整数
* 可以指定生成的范围和间隔
* stop位不取入范围内

### 函数
* 写法
def funcNam(param1,param2,...):
    xxx
    return xxx  # 可选

* 参数 ： 可变参数，默认参数
* 返回值：没有返回值、一个返回值、多个返回值

### 模块
* 导入模块 
1. import xxx(一般放在开头位置)
2. from xxx import ...

* 导入模块并重命名
from xxx as x 
from xxx import ... as x

* 引用

#### 安装模块(pip)
* pip install xxx

* 在vscode中终端配置 git bash 默认选项
* 步骤：
    文件→首选项→设置→Terminal→找到External: Windows Exec自定义要在 Windows 上运行的终端→"terminal.integrated.shell.windows": "C:\\swdtools\\Git\\bin\\bash.exe"(设置bin文件夹中的bash.exe的路径)

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 任务
* 使用flask 库，建立一个网页
* 路由： / 该页面下显示 hello world
* 路由 /xxx 该页面显示 hello,xxx!
* route()装饰器的第一个参数是URL规则，用字符串表示，必须以 斜杠（/）开始。这里的URL是相对URL（又称为内部URL），即不包 含域名的URL。

* 命令输入：env FLASK_APP=hello.py flask run(xxx.py是python源文件)
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)
```
注意： 
1. 第一行，导入模块
2. 第2行：Flask需要一个参数，这个参数通常是主模块或是包的名字。所以通常会传入 __name__
3. MVC理念
```python flask
    M：Model ==> 数据库模型
    V：Views ==> 可以理解为定义网页的地址，以及渲染网页等
    C：Controller ==> 可以理解为 网页功能的逻辑，实现

    这里就是其中V，就是路由。这里的代码的目的就是为我们来指定一个路由，也就是页面的地址。
    我们把**传入 app.route 装饰器的参数称为 URL 规则**。
```
4. 第4-5行: 使用app.route()装饰器会将URL和执行的视图函数(函数 index )的关系保存在app.url_map属性上。当你访问指定的URL时，就会调用这个函数。当遇到第一个return时，就会结束。其中的return就是你的response。

5. 第6-7行： 执行app.run来启动服务器。默认的Flask会监听的地址是127.0.0.1:5000。我们指定host和port参数，就修改了监听地址。 服务启动后，会先判断参数host以及port是否为None，如果为None，就会将host和port修改为默认值。然后会判断debug。然后就会调用werkzeug.serving.run_simple来启动Web服务，默认会使用单进程的werkzeug.serving_BaseWSGIServer来处理客户端的请求。

6. 调试模式1和2
    * app.debug = True
      app.run()
    * app.run(debug=True)

* 注意： Flask是基于**Werkzeug**开发的。

7. url_for 需要继续努力学习，还没搞懂~~

    
