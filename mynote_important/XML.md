## XML 语言基础

1. XML 语言声明-文档声明

    <? xml version="1.0" encoding="utf-8" standalone="yes" ?>

    standalone : 是否引入外部文件，yes : 不引入；no : 引入。

2. XML 元素

    1. XML 元素是未定义的。
    2. XML 命名规范。

3. XML 注释

4. XML 转移字符

5. XML CDATA 区

    CDATA中的内容，视作普通文本。
    <![CDATA[文本内容]]>

6. XML 的处理命令(PI:Processing Instruction)

    <? xml-stylesheet type="text/css" href="aaa.css" ?>

7. XML 语法规则概括：

    1. 所有 XML 元素都须有关闭标签
    2. XML 标签对大小写敏感
    3. XML 必须正确地嵌套顺序
    4. XML 文档必须有根元素(只有一个)
    5. XML 的属性值须加引号
    6. 特殊字符必须转义 --- CDATA
    7. XML 中的空格、回车换行会解析时被保留

8. XML 的DTD(Document Type Definition) 约束

    * 编写一个文档来约束一个XML的书写规范，这个文档称之为约束。

    * 两个概念：

        1. 格式良好的XML：遵循XML语法的XML
        2. 有效的XML：遵循约束文档的XML

    * 约束文档定义了在XML中允许出现的元素名称、属性及元素出现的顺序等等。

    * DTD 的三种类型
    
            使用内部DTD
           <!DOCTYPE  根节点  [   DTD的代码  ]>
            使用外部DTD
           <!DOCTYPE  根节点  SYSTEM  “DTD的地址”   >
            使用网络DTD
           <!DOCTYPE  根节点   PUBLIC   “DTD的名称”  “DTD的地址” >

    * 引入外部DTD 文档：
```java
        1. 当引用的DTD文档在本地时，采用如下方式：
        <!DOCTYPE 根元素 SYSTEM "DTD文档路径">
    
        如：<!DOCTYPE 书架 SYSTEM “book.dtd”>

        2. 当引用的DTD文档在公共网络上时，采用如下方式：
        <!DOCTYPE 根元素 PUBLIC "DTD名称" "DTD文档的URL">
```
   
   * DTD 定义元素
  
```java
    在DTD文档中使用ELEMENT关键字来声明一个XML元素。
    语法：<!ELEMENT 元素名称 使用规则>
    使用规则：
    (#PCDATA):指示元素的主体内容只能是普通的文本.(Parsed Character Data)
    EMPTY：用于指示元素的主体为空。比如<br/>
    ANY:用于指示元素的主体内容为任意类型。
    (子元素)：指示元素中包含的子元素
    定义子元素及描述它们的关系:
    如果子元素用逗号分开，说明必须按照声明顺序去编写XML文档。
    如: <!ELEMENT FILE (TITLE,AUTHOR,EMAIL)
    如果子元素用“|”分开，说明任选其一。
    如:<!ELEMENT FILE (TITLE|AUTHOR|EMAIL)
    用+、*、？来表示元素出现的次数
    如果元素后面没有+*?:表示必须且只能出现一次
    +:表示至少出现一次，一次或多次
    *：表示可有可无，零次、一次或多次
    ?:表示可以有也可以无，有的话只能有一次。零次或一次
    如： <!ELEMENT MYFILE ((TITLE*, AUTHOR?, EMAIL)* | COMMENT)> 
```

9. 属性(ATTLIST) 定义
```java
    <!ATTLIST 元素名称
        属性名 属性类型 约束
        属性名 属性类型 约束
        ...
    >
    example: 
    <!ATTLIST 商品
        类别 CDATA #REQUIRED 必须的
        颜色 CDATA #IMPLIED 可选的
    >
    对应的XML 为： <商品 类别=“服装” 颜色=“黄色”>

    属性类型：
    1. CDATA ：普通文本
    2. ENUMERATED ：枚举，只能从枚举的各项中选取。(鸡肉|牛肉|狗肉...)
    3. ID : 属性的取值不能重复(只能由字母,下划线开始)

    设置说明：
    1. #REQUIRED ：必须出现(类似mysql 的not null)
    2. #IMPLIED ： 属性可有可无(类似 mysql 中的数据可以是null)
    3. #FIXED ： 属性的取值固定()
    4. 直接值 ： 属性的取值为该默认值(赋值后，就可以当做常量)
```

10. 实体引用
```
    1. 语法：<!ENTITY 实体名称 "实体内容">

    2. 引用方式：&实体名称;

    3. example :
        <!ENTITY copyright "张三所有">
        XML引用： &copyright;

```

## MyEclipse中如何添加web.xml文件？
    * 在需要添加web.xml文件的项目上右键点击，依次选择MyEclipse->Generate Deployment Descriptor Stub，即可生成web.xml