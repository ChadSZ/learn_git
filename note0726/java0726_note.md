#### 修改myeclipse的主题背景

[下载地址](http://eclipsecolorthemes.org/?view=theme&id=93)

1. 使用前建议备份当前的配置，File-->Export-->General-->Preferences
  点击下一步，将这个配置文件导出任意文件夹下，如former.**epf**

2. 将下载好的EPF配置文件导入，File-->Import-->General-->Preferences就是上一步的逆操作

#### 面向对象的思维
首先分析这个问题里面有哪些类和对象，这是第一点，然后再分析这些类和对象应该具有哪些属性和方法。这是第二点。最后分析类和类之间具体有什么关系，这是第三点。

面向对象有一个非常重要的设计思维：合适的方法应该出现在合适的类里面

#### 面向对象的理解
对现实事物的抽象，抽象出事物的属性filed(成员变量)和行为method(函数)以及特殊的构造器constructor。

属性field ：**[修饰符] 属性类型 属性名 = new 属性类型()**;通过这样来创造一个**instance(实例)或者说对象**。

通过方法是无法分辨两个实例是同一个对象，而其具备的具体属性是不一样的，每个对象都有自己的属性。

类和对象的理解
```Java
类：一类事物的抽象，抽象包括该类事物的属性和行为，是一类事物的模板。

对象：是对某一类事物的具体，具体到该类的某一实例instance。
```


类与类之间是有关系的，
关系：

关联关系，是最弱的一种关系

继承关系，AAAAXX是XX的一种(学生是人，老师是人)

聚合关系，AAAXX是XX的一部分

     * 聚集关系：队员和队伍
     * 组合关系：身体和身体器官

实现关系,子类实现父类

多态关系，![图来展现多态关系](https://pic1.zhimg.com/80/v2-3efe573f18aafbad6d92aeb0f44eedfc_hd.jpg)

[面向对象的三个基本特征](https://mp.weixin.qq.com/s?src=11&timestamp=1564125093&ver=1751&signature=Z9OmBtKCdCzleqh3A1XVkvkNGW5neMY68Caj7RisgPqNbfNlZOvTRM4Ih9bqdnfkGoXhBvluppUaGBzxuGUTOuOvDaTNDfLfG07knDQn8uyiKUGt0-tjthV*tCTYhNvI&new=1)



软件的开发：如何达到**可重用性（reusable），可扩展性**的境界呢？

#### 构造器
当我们在重载构造器时，重载了有参的构造器，那么无参构造器必须写上去，这是**规定**。

#### this的功能
1. 在程序中产生二义性之处，赢使用this来致命当前对象；普通方法中，this总是指向
2. this和重载的共同使用。

#### static静态变量(全局变量定义)
```java
public static int num;
```
#### 静态导入
```java
import static java.lang.Math.*;//导入Math类的所有静态属性。
```
```java
    System.out.println(""+int1+int2);
    输出的是一个字符串。
```
注意：**this和super不能同时使用**。