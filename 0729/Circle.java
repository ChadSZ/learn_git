package area_perimeter;

import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;

public class Circle {
	
	private double radius;
	public static final double PI = 3.14;
	/**
	 * @param args
	 */
	public Circle(){
		super();
	}
	
	//获取面积方法
	public void getArea(double rad){
		
		double s = PI * rad * rad;
		s = new BigDecimal(s).setScale(2, BigDecimal.ROUND_HALF_UP).doubleValue();		
		System.out.println("圆的面积为："+s);
	}
	
	//获取周长方法
	public void getPerimeter(double rad){
		double p = PI * rad * 2;
		p = new BigDecimal(p).setScale(2, BigDecimal.ROUND_HALF_UP).doubleValue();
		System.out.println("圆的周长为："+p);
	}
	
	//显示操作
	public void show(){
		radius = ScannerTest();
		getArea(radius);
		getPerimeter(radius);
	}
	
	public static void main(String[] args) {
		Circle circle = new Circle();
		circle.show();
	}
	
	//scanner类可以实现键盘输入功能
	public static double ScannerTest(){
		Scanner sc = new Scanner(System.in);
		System.out.println("请输入圆的半径："	);
//		 int radius = sc.nextInt();
		float radius = sc.nextFloat();
//		 System.out.println("圆的半径为："+radius);
		 return radius;
	}

}
