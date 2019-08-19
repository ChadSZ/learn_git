## EL 表达式

注意：

    1. EL表达式只能获取数据。
    2. 仅在JSP 的静态页面获取数据。

* EL 表达式语法格式： ${标识符}


* 以标识符为关键字从各个域对象中获取对象。

* EL 只能从四大域中获取数据。其查找数据的顺序是，依次从小到大的范围从四大域中查找指定名称的属性值。

    四个域的作用域范围大小:PageContext （page域） < request < session < servletContext（application域）

* 访问Bean 的属性：

    EL可以通过${key.属性}的方式获取到指定对象的指定属性值。其底层实际调用的是对象的相应属性的get 方法。(或${key["属性"]})

* EL 访问数组：

* EL 访问 list , set(不可以访问) , map 


* 关于1.8JDK：

    **jsp中的EL语言是否需要在创建对象的泛型中写入详细泛型？**

    如： Map<String,Object> map = new HashMap<？？？>();


* EL 运算符：

    1.  算术运算符：+-*/%(不支持++，--)
    2.  关系运算符：==、!=、>=、<=
    3.  逻辑运算符：! && || not and or
    4.  条件运算符：? :
    5.  取值运算符：[] .

    6. empty :${empty 变量},其结果为boolean型

            <!-- empty对于没有定义的变量的运算结果为：true -->
            empty name = ${empty name }<br/>
            
            <!-- empty对于为null的引用的运算结果为：true -->
            empty username = ${empty username }<br/>
            
            <!-- empty对于空串的引用的运算结果为：true -->
            empty schoolName = ${empty schoolName }<br/>
            
            <!-- empty对于没有元素的数组或集合的运算结果为：true -->
            empty students = ${empty students }<br/>


* EL 的内置对象

    EL有11个内置对象，(包括四大域)

    1. Page、Request、Session、application...


```java
1. action :
   1. <form action="registerServlet" method="POST">
   
        action的路径为相对路径，如果有"/"的话，说明是在web服务器的根目录。
        不带"/"，是当前访问路径的资源路径。

    2. <form action="${pageContext.request.contextPath }/registerServlet" method="POST">

        底层实际调用的是pageContext.getRequest() 方法。
        **获取当前web应用的根，即：获取当前项目的发布到服务器的名称**。对于pageContext应用最多的。
   
```

    2. 在EL 的11个内置对象中，除了pageContext外，其它10个内置对象，其类型均为java.util.Map 类型。



## MyEclipse中如何添加web.xml文件？
    * 在需要添加web.xml文件的项目上右键点击，依次选择MyEclipse->Generate Deployment Descriptor Stub，即可生成web.xml

* EL 不支持对字符串操作。



## 自定义EL函数 获取处理字符串功能

1. 定义函数
2. 注册(*.tld文件下)
3. 使用(<%@ taglib uri="" prefix="">%)指令

* 注意：  EL函数只能处理四大域中的属性值及String常量(处理字符串时)


## JSTL 中的 EL 函数
* Apache 定义好一套标准的标签库规范，称为JSTL(JSP Standard Tag Library)，该规范已通过JCP审核认定。

    * JCP(Java Community Process) 是一个开放的 国际组织，主要由 Java开发者以及被授权者组成，职能是发展和更新。

* 在JSTL中，定义了16个对于字符串处理的函数。我们在JSP页面中可以直接使用。

* 导入Jar包。jstl.jar & standard.jar。
    
    [jstl导包及导包声明](https://blog.csdn.net/qq_30062589/article/details/80224080)