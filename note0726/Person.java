package Person;

public class Person {
	//类的属性
	private String name;
	private String sex;
	private int age;
	private static int num;
	
	//特殊的行为,constructor
	
	public Person() {
		//this("李四","男",11);
		//System.out.println("这是一个构造器方法");
		
	}
	public Person(String name,String sex,int age){
		this.name = name;
		this.age = age;
		System.out.println("姓名："+name+",性别："+sex+",年龄："+age);
	}
	
	//类的行为
	public void run(){
		System.out.println("I can run");
	}
	public void speak(){
		System.out.println("hahaxixihehe");
	}
	public void job(){
		System.out.println("I have two jobs");
	}
	public void display(String name,String sex){
		System.out.println("姓名："+name+",性别："+sex);
	}
	
	public static void main(String [] args){
		//Person p1 = new Person("张三","女",24);
		Person p1 = new Person();
		//p1.run();
		//System.out.println(Person.num);
		p1.display("小强", "male");
	}
}
