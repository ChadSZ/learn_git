package area_perimeter;

import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;

public class Circle {
	
	private double radius;
	private double hight;
	public static final double PI = 3.14;
	/**
	 * @param args
	 */
	public Circle(){
		super();
	}
	
	public double getRadius() {
		return radius;
	}

	public void setRadius(double radius) {
		this.radius = radius;
	}

	public double getHight() {
		return hight;
	}

	public void setHight(double hight) {
		this.hight = hight;
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
	
	public void getCylinder(float radius2, float hight2) {
		double volume = PI*radius2*radius2*hight2;
		volume = new BigDecimal(volume).setScale(2,BigDecimal.ROUND_HALF_UP).doubleValue();	
		System.out.println("圆柱体的体积为："+volume);
	}
	
	//显示操作
	public void showVolume(){
		ScannerTest();
	}
	
	public static void main(String[] args) {
		Circle circle = new Circle();
		circle.showVolume();
	}
	
	//scanner类可以实现键盘输入功能
	public void ScannerTest(){
		Scanner sc = new Scanner(System.in);
		
//		System.out.println("请输入圆的半径："	);
		System.out.println("请输入圆柱的底面半径和高：");
		
		//输入圆半径
		float radius = sc.nextFloat();
		System.out.println("输入半径为："+radius);
		
		//输入圆柱高
		float hight = sc.nextFloat();
		System.out.println("输入高为："+hight);
		
		//获取圆面积
		getArea(radius);
		//获取圆周长
		getPerimeter(radius);
		//获取圆柱的体积
		getCylinder(radius,hight);
		
	}


}
