### list && dict

#### 查看长度函数 len
* len函数可以查看字符串、列表、集合、tuple、dict长度

#### 关键词 in：判断是否在内部存在该元素
"a" in "abcdef"

"a" not in "abcdef"

#### 数据类型 2
1. 列表 "list"
##### 增查改删
* 表示方法 [element1,element2,element3...]
* 从左往右：通过索引index 来访问其中的元素 list[index], index 从0开始
* 从右往左：index 从-1开始，最小索引为 - len(list)
* append 函数插入一个元素到list中。list.append(element)
* pop 函数删除指定索引的元素。list.pop(i),默认删除末尾的元素
* 列表的连接功能 使用 **+**

    list_a = [1,2]
    list_b = [2,3]
    list_c = list_a + list_b
    print(list_c)
* 更新指定索引对应的值 list[index] = newValue

* 练习任务：新建一个100个相同元素的列表

#### 在dos命令行运行.py程序出现：File "<stdin>", line 1
* 原因： 
在shell脚本中，运行shell脚本命令；在Python命令行中，运行Python代码。然而，“python hello.py”是一个脚本命令，不是python代码。

因此，**退出python命令行，直接cd到hello.py所在目录**，运行python hello.py，即可。

2. 字典"dict"
* 由键值对构成的{key1:value1,key2:value2}
* 查询指定keyx的value : dict[keyx]或者是
dict.get(keyx),dict.get(keyx)[keyxx]
* 增加一对键值对，直接复制dict[newKey] = newValue
* 修改指定key的value，赋值dict[key] = newValue
* 删除一对键值对dict.pop(key)

* 注意： 低版本的python可能是乱序的！

3. 元组 "tuple"
* 初始化(element1,element2,element3...)
* 元组内容一旦初始化，便不能更改

4. 集合 "set"
* set()元素是不会重复的，和数学中的集合概念很类似
* 作用1：取出一个list里面的重复元素
* 作用2：交集、补集、差集：对比两个list中的相同元素，不同元素。
difference/union/intersecton

#### 条件语句

if condition:
    xxxx
else:
    xxxx

if condition:
    xxxx
elif:
    xxxx
else:
    xxxx

* 请用户输入一个成绩，判断优秀(>=90)、良好(80-89)、一般(60-79)、不及格(<60)。

## 任务

1. 输入三条边的长度，如果能构成三角形就计算周长和面积。
2. 用户身份验证用户名和密码，管理员、用户、超级用户。
已知管理员身份的有以下：方开-123，刘晨-12345；
超级用户：张旭-123321、沈章-123456、许景-123456
访客：其他(字母或者中文构成的用户名)-guest
输出：访问成功，访问失败

### 任务中遇见问题：
* TypeError: float() argument must be a string or a number, not 'list'
```python    
具体原因：float这些基本类型不能用于列表list
如，tri_edge1,tri_edge2,tri_edge3 = float(input("分别输入三条边长：").split(','))
```
### 自学知识点 map()函数

* map(func, seq1[, seq2,…])

1. list [1, 2, 3, 4, 5, 6, 7, 8, 9]
    如果希望把list的每个元素都作平方，就可以用map()函数：
    因此，我们只需要传入函数f(x)=x*x，就可以利用map()函数完成这个计算

2. 注意：map()函数不改变原有的 list，而是返回一个新的 list。
利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。

3. 
***将元组转换成list***
>>> map(int, (1,2,3))
[1, 2, 3]
***将字符串转换成list***
>>> map(int, '1234')
[1, 2, 3, 4]
***提取字典的key，并将结果存放在一个list中***
>>> map(int, {1:2,2:3,3:4})
[1, 2, 3]
***字符串转换成元组，并将结果以列表的形式返回***
>>> map(tuple, 'agdf')
[('a',), ('g',), ('d',), ('f',)]
#将小写转成大写
def u_to_l (s):
 return s.upper()
print map(u_to_l,'asdfd')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def f(x):
    return x*x
map1 = list(map(f,list1))
print(map1)

### 自学知识点 比较字符串大小
```python
# 下面的 id 和 is 都是用来判断对象的
# if username[0] is a or username[1] is b:
# if id(username[0]) == id(a):
#     if id(userpass[0])==id('123'):
# 而下面是用来比较字符串内容的
if username[0] == a or username[1] == b:
```
注意： **python中没有自增自减！**
**python中没有大于等于这类的符号！**