### 知识解答
#### cmd为什么可以编译.cpp和.java？
    为环境搭建了JDK的环境变量，故可以使用dos命令行来编译和运行java的文件。


#### 文档注释，单行多行注释，以及行内注释
   文档注释

    /**
	 * @param args
	 * @throws Exception 
	 */

 单行多行注释

    // &&   /*
            */

行内注释

    /*aaaa*/

#### Java的命名：

    java使用 英文，$ , _ , 不能使用数字开头。

#### Java的基本数据类型：

    byte        1byte        (byte)0
    short       2byte        (short)0
    int         4byte        0
    long        8byte        0l
    float       16byte       0.0f
    double      32byte       0.0d
    boolean                  false
    char        1byte       \u0000 null

注意[boolean类型的长度](https://blog.csdn.net/qq_35181209/article/details/77016508)：1bit 1byte 4bytes



#### Java的关键字
public class void static private switch case for do while if else try catch finally byte short int long float double boolean char string println out  ...

static：

    1. 修饰全局变量
    2. 静态方法
    注意： 静态变量只能被静态方法调用。
    静态变量同样可以被 `类名.静态变量` 调用。

`Java是一种强类型语言。如，int a = 3; 
a在申明后，在不被强制转换的情况下，就一直是int类型。`

#### 变量的分类

    类型        声明位置        从属于      生命周期
    局部                      方法方法快
    全局                        类
    成员                        对象

#### 常量

    final来声明
    如，final double PI = 3.14;

#### 运算符 & 算术运算符

    + - * / % 
    ++ --
    += 
    & && | || ^ ! 
    < > <= >= != ==
    << >> <<< >>>
    ()
    优先级注意

#### 数组
    声明与创建
    ArrType[] Arr;
    ArrType[] Arr = new ArrType[10];
    ArrType[] Arr = new ArrType{aa,bb,cc};

##### 遍历数组
    for(int i=0;i<10;i++){}
    for(ArrType Arr : ArrObj){}(foreach)

##### 多维数组
```java
    ArrType [][] arrs = new ArrType[3][3];
    ArrType [][] arrs = {};
```
#### 字符串

##### 字符串的比较（== .equals）
```java
    String str1 = "abcde";
    String str2 = "abcde";
    String str3 = new String("abcde");
    syso(str1 == str2);
    syso(str1 == str3);
    syso(str1.equals(str3));
```

##### classpath需要安装吗？
    在低版本需要安装，而在高版本不需要，因为path环境变量中，已经打包了。