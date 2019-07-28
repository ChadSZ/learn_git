### js
1. 为什么出现了JavaScript？

    + 如果将计算全部放在服务端进行，会导致页面的刷新过慢，所以会在浏览器端实现简单的运算和判断，而Javascript实现了该功能。
2. Java和Javascript的关系
    + 两者没有直接的联系，JS仅仅吸收了部分Java的特点。
3. Javascript的特点
    + JS是解释型语言，不需要编译。
4. js是静态文件，jsp是动态文件，两个都可以用来保存复用函数。
    + 放在jsp文件里可以获得比较好的灵活另，例如实现国际化，将js写在jsp文件里然后配合struts的标签是很容易实现的，但是这在js文件里就很难做到。
    + js文件也有一个优点，就是可以让客户端缓存。如果这个函数放在jsp文件，然后在每个页面都include它，那么每次页面加载时都将重复下载这部分代码。

        但是，如果放在js文件的话，那么客户端在第一次引用该函数时下载js文件，在后面的使用中发现路径相同就直接引用本地缓存的js文件。因为它是静态文件所以能够缓存。
    + 总结一下，放在js文件可以降低网络传输量，所以，如果不是为了必须的灵活性，应该尽量使用js文件来保存javascript代码。

5. JS变量
* JS是弱类型，通过var i=0;来声明变量
* 可以不用var来声明变量，直接用，这样的变量就是全局变量，如非特殊需要，尽量先声明
* 声明字符串：可以使用双引号声明字符串，也可以使用单引号声明字符串。如，var str = "aaa"; 或者 var str = 'aaa';

6. JS函数声明
* 不需要声明返回值类型、参数类型。函数定义以function开头。
函数声明如，
```html
function add(i1,i2){
	return i1+i2;
}
```

7. JS面向对象
* JS中没有类的语法，js中String、date等“类”都叫做“对象”,如下声明
```html
function Person(name,age){
    this.name=name;
    this.age=age;
    this.SayHello=function(){
alert("你好，我是"+this.name+"，我"+this.age+"岁了");
    }
}
var p1=new Pweson("tom",20);
p1.SayHello();
```



### Html的框架结构
```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <script type="text/javascript">       
    </script>
</head>
<body>
    
</body>
</html>

```