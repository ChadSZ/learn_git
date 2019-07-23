# note
## Python简单介绍:
 设计者：Guido van Rossum

（集合了ABC、module等语言的优点 ）

* python的特点：简单易学，开发效率高，清晰易读，免费开源，可移植，可扩展，库强大
* 执行效率慢，2与3不兼容

## python应用：
人工智能，云计算，WEB开发，网络爬虫，网络编程，数据分析，科学计算，自动化运维

### python安装：
1. add python 3.7 to path添加到环境变量中。
2. 不需要自定义安装，直接默认安装即可。
3. 命令行输入pip -v可以查看当前python状态


提及到python的pyqt框架


## IDLE：交互式环境

### 代码的创建及运行
```
1. 创建文件，并保存
2. 输入代码
3. Shift+右击，打开powershell或者使用git bash命令
4. 运行各种方式：
 * Python + 文件名首字母+tab可以运行自己的.py文件
 * 在命令行输入python，再将文件拖入命令行中，可以发现同样可以运行该程序。
 * 或者在编辑器IDLE中，快捷键F5可以直接运行，或使用run。
 * 在vscode中运行.py文件，右击然后可以直接`在终端运行`（首先，得安装python插件）
```

 ###vscode中新增插件
 * 添加`code runner`，可以一键运行(`ctrl+alt+n`)( 可用于C, C++, Java, JavaScript, PHP, Python, Perl, Perl 6, Ruby, Go, Lua, Groovy, PowerShell)

 ###vscode中的单多行注释
 ```python
    # HELLO WORLD 这是一个单行注释
    print("hello world"); #这也是一个单行注释
 ```
 ```python
  ...
    这是一个多行注释 
    print(1);
  ...

 ```
 ```python

    quit();
    这是一个退出python命令行的命令
 ```

## 自学部分
### pip的解释
   pip是Python官方推荐的包管理工具:
   属于python的一部分。
### 如果需要升级pip，有以下2种方式：
   1. python -m pip install --upgrade pip
 python 升级 pip命令行输入：python -m pip install --upgrade pip
   2. easy_install.exe pip 9.0.2

```
### 说明：
在使用python的时候，经常使用到pip这个工具，可以很方便的线上安装依赖库，当然pip还有很多参数都可以帮我们去查询一些库信息，这里就不说pip的安装了，还是提供下思路，在安装python的时候，下载带有pip的安装包就可以直接安装pip啦，当然没有带pip的，也可以通过下载安装包，手动安装。手动安装还是要会的，毕竟有时候下载超时、或者安装失败都可以用。命令：python  库的setup.py install

1. 查看pip

   （1）直接在cmd窗口中输入pip命令，会显示pip所有的参数使用方法；

 
   （2）输入pip提示Did not provide a command，则有两种可能，第一是没有配置环境变量，第二就是其他应用程序也存在pip的环境变量
 
   
2. where pip

这个命令不是pip的命令啊，用这个命令主要是如果上一步，环境变量配置没问题，就是第二种啦，这时候就可以用where pip来查询啦
 
上图可以看到，有三个pip，所以直接输入pip系统无法识别是其中某个。怎么可以快速解决呢？输入pip.exe即可，当然也可以去到pip.exe的路径下，输入pip也行

3. pip版本

   用pip -V可以查看版本，是大写的V：

 pip版本升级命令：pip install --upgrade pip
升级命令用的不多，一般如果是python自带的pip版本，可能会比较低，使用pip安装第三方库就会出现报错，但是报错的最后会给出这个升级命令，还是比较贴心的。

4. pip list

查看已经安装的第三方库

 pip list --outdated：可以查看有新版本的第三方库，可显示现在安装的版本，以及最新的版本


5. pip安装第三方库
命令：pip install  库名

pip安装会拉取最新版本安装，想安装任意版本则可加上版本号
命令：pip install 库名=版本号
 

6. 查看安装

查看安装库的详细信息，命令：pip show 库名
 

7. 卸载第三方库

命令：pip uninstall 库名

8. 卸载pip

卸载pip的命令：python -m pip uninstall pip；也可以直接把pip文件夹删了；建议使用命令后把遗留的文件删除即可。

9. 通过pillow安装PIL
```