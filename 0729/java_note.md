### java
#### 静态变量修饰及调用
##### public static int id;
* 通过类名调用(class1.id = id)

####静态方法的调用
* 同样可以通过类名调用(class1.method1())


#### 成员变量
*通过this.name = name;调用

#### 权限修饰符
* public private default protected
1. private 
被private修饰的成员仅能在其修饰的贝类使用。
2. default
其只能被本类以及同包下的其他类访问。
3.protected
其只能被同包下的其他类访问。如果不同包下的类要访问被protected修饰的成员，这个类必须是其子类。
4. public
可以被任意包中的任意类所使用。

#### 继承 extends


#### 编程题
编写应用程序，创建类的对象，设置圆的半径，计算并分别显示圆半径、圆面积、圆周长。


#### 涨姿势啦~~ Scanner
```java
  /** 
   * Scanner类中的方法 
   * 优点一: 可以获取键盘输入的字符串 
   * 优点二: 有现成的获取int,float等类型数据，非常强大，也非常方便； 
   */
  public static void ScannerTest(){ 
    Scanner sc = new Scanner(System.in); 
    System.out.println("ScannerTest, Please Enter Name:"); 
    String name = sc.nextLine();  //读取字符串型输入 
    System.out.println("ScannerTest, Please Enter Age:"); 
    int age = sc.nextInt();    //读取整型输入 
    System.out.println("ScannerTest, Please Enter Salary:"); 
    float salary = sc.nextFloat(); //读取float型输入 
    System.out.println("Your Information is as below:"); 
    System.out.println("Name:" + name +"\n" + "Age:"+age + "\n"+"Salary:"+salary); 
```
#### 涨姿势啦~~ 保留小数点位数
```java
    double a=1.2356;
    //方法1
    double b=(double)Math.round(a*100)/100;  //1.23
    //方法2
    String s1=String.format("%.2f",a);  //1.23
    //方法3
    DecimalFormat df=new DecimalFormat("#.##");
    String s2=df.format(a);  //1.23 //如果a=1.2结果为1.2
    //方法4
    DecimalFormat df2=new DecimalFormat("#.00");
    String s3=df2.format(a);  //1.23 //如果a=1.2结果为1.20
    //方法5
    NumberFormat nf=NumberFormat.getInstance();
    nf.setMaximumFractionDigits(2);
    nf.setRoundingMode(RoundingMode.DOWN );//down不四舍五入，up四舍五入
    String s4=nf.format(a);    
    //down  a=1.2356    s4 =1.23 
    //up       a=1.2356    s4 =1.24 

```
