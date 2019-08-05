### java 常见报错
* java.lang.String can only be extended by a subclass,a superInterface must be a interface;

String 类型只能被其子类继承，一个父接口必须是一个接口。

* cannot be resolved to type:被引用的类型

* Abstract methods do not specify a body

抽象方法不能做实现。

* the abstract method sleep in type a can only be defined in a abstract class;

抽象方法只能定义在抽象类中。

* Syntax error on token "implements", extends **expected**：

实现的语法错误，建议使用继承

* Illegal modifier for the interface C; only public & abstract are permitted：

无效的权限修饰符，仅允许使用 public & abstract。

**注意：接口中可以定义全局变量。但不建议。**
### java 的 has a 和 is a
* B is a D(继承); B has a C(B类中包含C)


### 访问属性的方法：
1. get属性和set属性 
2. 构造器访问属性
3. 类名.属性 (不推荐，安全性要求上，会使用private,而在外面调用，不可行)

### javaBean
1. javaBean 格式
    属性：private 修饰符修饰
    行为：public 修饰符修饰
    得到属性，通过行为的get/set 来获取

### java 的包操作：
* 创建Jar包

选择工程文件 → export → Jar file → 保存路径

* 引用jar包

右击另一工程文件 → 创建lib文件夹 → 将jar包复制到该文件夹内 → build path ：add to ... → 在该工程文件即可引用该jar 包

* 删除jar包

右击加入的jar包 → build path : remove from build path → 删除lib 中的Jar包