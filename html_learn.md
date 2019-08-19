## 标签

* label ：对label 元素点击文本标签，会触发内部控件。实现关联功能。
  
* aria-label : 当 input 组件获得焦点时，屏幕阅读器会读出相应的label文本。

* aria-labelledby ： 当想要的标签文本已在其他元素中存在时，可以使用aria-labelledby，并将其值为所有读取的元素的id。

* background-attachment: scoll,fixed

* type = "email" ：该类型是email类型，即必须加@。

* required :必填项

* autofocus :自动光标定位到该处

* form-control ：bootstrap 自定义的文本框类型设置。

* onblur : 当用户离开输入字段时对其进行验证。



## class 和 id 的清晰的区别：

1. class(类)在同一个html网页页面可以无数次的调用相同的class类;ID是表示着标签的身份,所以ID在页面里也只能出现一次，并且是唯一性。
2. class是以小写句号"."开头命名，而ID是以"#"开头定义。
3. id 和 class 命名最好以英文开头。

## class = "sr-only",screen reader only
* 说明：用于为视觉残疾人员，可以"读出"屏幕图片。

## margin 的默认顺序：
* 上右下左：顺时针。

1. 如果没有left值，则使用right代替；

2. 如果没有bottom值，则使用top代替；

3. 如果没有right值，则使用top值代替。

## 边框的宽和高的计算

* div的类wrapper如下的css样式：

1. 情况：
   
        .wrapper{
            
            width:100px;
            height:100px;
            background:pink;
            padding:10px;
            border:1px solid black;
            margin:10px;
        } 
    ![通过图片来观察](https://pic2.zhimg.com/80/v2-6b3b1b4bcb52ed168ed8884834385be9_hd.jpg)

    height = 100 + 10 * 2 + 1 * 2 = 122

2. 情况：
   
        *{
        margin:0;
        padding:0;
        box-sizing:border-box;
        }
        body{
        border:1px solid blue;
        margin:10px;
        }
        .wrapper{
        width:100px;
        height:100px;
        background:pink;
        margin:10px;
        padding:10px;
        border:1px solid black;
        }

    ![通过图片来观察](https://pic2.zhimg.com/80/v2-8bb899801a91038e642a2d3eb9bb132d_hd.jpg)

    * 注意： 此时 div.wrapper 元素的宽高还是 100*100，但实际内容区的宽高变成 78*78，元素的宽高包括实际内容的宽高加上 border 和 padding 的值

3. 情况：

         *{
        margin:0;
        padding:0;
        box-sizing:content-box;
        }

    此时 div.wrapper 元素的宽高为 122*122 ，内容的宽高还是100*100

    ![通过图片来观察](https://pic1.zhimg.com/80/v2-8a30fe5465a6ef528980852ba37f5730_hd.jpg)

* 需要注意： box-sizing:

        -moz-box-sizing:border-box; /* Firefox */
        -webkit-box-sizing:border-box; /* Safari */


## position 文档流及位置属性

[具体图解请看](https://zhuanlan.zhihu.com/p/29116007)

* 文档流(普通流)：相对于窗体自上而下分成一行一行，并在每行按照自左往右的顺序排放元素，即为文档流。每个非浮动块级元素都独占一行，每个浮动元素按照规定的浮动方式浮动在行的一端，都不会独占一行，当一行无法放下该元素，则会从下一行继续按浮动方式排序。


* 包括任意的元素(块级、内联、列表元素)都可以生成子元素，在其内，形成文档流。

* 默认static ：没有定位，忽略top,bottom,left,right 以及z-index。符合文档流的排序。

* absolute : 脱离文档流，相对于一个非static 的父元素进行定位(其父元素是position:relative/fixed/absolution)。生成绝对定位的元素，仍然是相对于文档进行排列的。如果它的父级元素和爷爷级上级元素都是非position:static 属性，则会选择最近的父元素进行定位。

* relative : 没有脱离文档流，相对于它本身在文档流中的位置，进行定位的。

* fixed : 脱离文档流，相对于整个浏览器窗体而定位的，原来文档流中不存在其位置。
  




## 堆叠高度

* z-index: 设置该内容在页面的相对高度

    1. 在当前元素位置创建堆叠上下文，即告诉浏览器这里出现了堆叠，需要考虑分层。
    2. 告诉浏览器在这个堆叠上下文中，这个元素所处的分层位置。

    * 默认z-index = auto; 按照先后次序进行堆叠。
    * 子元素要服从父元素的堆叠高度。


## 矩形圆角

* 

* 题目： [有些复杂图形不能利用border-radius,我们该如何做呢？](https://zhuanlan.zhihu.com/p/34507909)


## 按钮组

1. button:

    * btn 样式

      1. btn-block(width=100%)
      2. btn-default
      3. btn-primary
      4. btn-danger
      5. btn-success
      6. btn-info
      7. btn-link
     

## form 表单

* 当点击form内部的submit按钮时，可以提交表单数据到action指定的位置。

* form表单的method="get/post" ，分别对应了http 上的get 和 post 方法。

    1. get :

        是form的默认方式。

        用于从服务器上获取数据，

        将表单中的数据按照variable = value 的形式，添加到action后的url后面，并用? 连接，而各个变量之间用"&"连接。

        get 是不安全的，因为在传输过程中，数据被放在了url中，而如今很多服务器，代理服务器或者用户代理都会将url记录到日志文件中，导致数据会被第三方看到。另外，用户可以直接看到提交的数据，一些系统的内部消息同样会出现在用户面前。

        get 传输的数据量小，因为受到url的长度限制

    2. post :
   
        向服务器传输数据，

        post是将数据放在form 的数据体中，按照变量和值对应的方式，传递到action所指向的url。

        post的所有操作对客户都是不可见的。

        post 可以传输大量数据，所以上传文件只能通过post。


## 属性及样式获取

* 如，获取<input type="text" id="btn" style="background-color: red"> 的属性和样式：

1. 获取type属性可以用： document.getElementById("btn").getAttribute("text"); //注意要获取的属性有双引号
2. 获取元素样式可以用： document.getElementById("btn").style.backgroundColor;


## jsp中写java代码有如下三种方式：

<%！ %>，这里面可以申明变量或方法，注意：这里面申明的变量是全局的

<% %>，与上面的方法相比，这个方法的局部的

<%= %>，用于输出表达式到浏览器，注意：这里面的表达式不能跟分号

## 关于page指令，我们平时见得最多的就是这样的：

1. page指令
    
    <%@page contentType="text/html;charset=gb2312" import="java.util.Date"%>

    主要用于：设置编码，导入jar包


2. include指令
   
    关于include指令，他用于引入其他jsp页面，jsp引擎会将两个jsp翻译成一个servlet，所以也称为静态引入


3. taglib指令
   
    关于taglib指令，是定义一个标签库以及其自定义标签的前缀。
    
    比如我们常用的c:foreach的使用。先导入jstl的包，然后在jsp中加入这个标签：<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>就可以使用c:foreach了


## form 表单
```java
1. action :
   1. <form action="registerServlet" method="POST">
   
        action的路径为相对路径，如果有"/"的话，说明是在web服务器的根目录。
        不带"/"，是当前访问路径的资源路径。

    2. <form action="${pageContext.request.contextPath }/registerServlet" method="POST">

        获取当前web应用的根，pageContext内置对象。对于pageContext应用最多的。
   
```