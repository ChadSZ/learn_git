## 文件和异常

### 读文件
* f = open("filePath","mode")
* mode:
    r:只读  read
    a:插入  append
    w:写    write

* 注意：如果在文本txt中直接创建写入数据，很有可能会发生中文乱码，最好在vscode中新建文件
* 读
    read()函数：默认读取文件所有内容
    read(size)：读取指定长度的元素内容
    readline(): 读取一行数据内容
    readlines(): 读取所有行内容，并将每行数据作为列表中的元素，并放入缓存区,返回list。

* 写
    write(): 默认覆盖之前所有内容

* 插入
    append(): 默认将数据放置在最后位置

* +:读写

### 读写操作流程
1. 打开一个文件 f = open(path,"mode")
2. 读写操作 f.read() / f.write()
3. 关闭文件 f.close()

### with ...
with open(filepath,"mode") as f:
    f.read() / f.write(something)

### 异常
try:
    code
except Exception:(Exception 所有异常的父类)
    ...
finally:/可选
    ...
* Exception 捕获所有异常
* 内置的异常类型，ZeroDivisionError,NameError,IndexError 等
* 注意： try 内部尽量减少语句，会提高效率


* \n\r： 换行符
* 注意：
1. git bash 相当于Linux 环境
2. 在vscode中运行不论是反斜杠还是正斜杠，抑或是 r + 反斜杠来使用同意也可以索引该目录。

1.
```python
a = [1,"1","2",2]
print(a[0]+a[1])
```
2.
```python
a = {"name":"shenzhang","age":11}
print(a[ages])
```
3.
```python
a = [1,2,3,4,5]
b = (1,2,3,4,5)
print(a+b)
```
### 任务
* [读写csv 文件](https://zhuanlan.zhihu.com/p/40937189)

    写入三栏

    姓名 年龄  性别

     a    11    男


* [读写json 文件](https://mp.weixin.qq.com/s?src=11&timestamp=1564639030&ver=1763&signature=Mw2XZwgw7m92YqaTItGh6AgH2PdLf06zaVr23Laic9hRoJirtUVwTUmnU67oktqhS68tXVQcQUHaBCkVYccmIhRd2*69DemDMHNA0wKngHzX2*jWgJo-hsu2ZK4GcUmx&new=1)(json(JavaScript Object Notation) 是一种轻量级的数据交换格式,用于字符串和python数据类型间进行转换)

将一个人的名字、年龄、性别保存成json格式的文件。

{

    "name":"fangkai",

    "age":"15",

    "sex":"male"
}


### 涨姿势啦~
使用 csv 写入 CSV 文件
也可以使用writer对象和 write_row()方法写入 CSV 文件：

1. delimiter指定用于分隔每个字段的字符，默认值为逗号（,）

2. quotechar指定用于包围包含分隔符字符的字段的字符，默认值为双引号（"）

3. escapechar指定用于转义分隔符的字符，以防引号未使用。默认值为无转义字符

* 如，csv.writer(csv_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

* json的模块功能：

1. Json模块提供了四个功能：dumps(dump string)、dump、loads、load

* Json的优势

1. 数据体积方面。

    JSON相对于XML来讲，数据的体积小，传递的速度更快些。

2. 传输速度方面。

    JSON的速度要远远快于XML

3. 数据格式

    数据格式比较简单, 易于读写, 格式都是压缩的。



### you-get 的安装及使用
* pip install you-get

* you-get xxxxx(仅用于视频或者图片的链接) 可以下载啦~

