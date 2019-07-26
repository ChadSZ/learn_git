package Person;
import java.lang.Math.*;
import java.text.*;
import java.math.*;
public class AreaPerimeter {
	private double r;
	public static final double PI = 3.14;
	public AreaPerimeter(){
		
	}
	public AreaPerimeter(double r){
		super();
		this.r = r;
	}
	public double getArea(){
		return(PI * r * r);
	}
	public double getPerimeter(){
		return(PI * r * 2);
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		AreaPerimeter ap = new AreaPerimeter(10.1); 
		double area = ap.getArea();
		double perimeter = ap.getPerimeter();
		System.out.println("未保留小数点位数"+"面积为："+area+"周长为："+perimeter);
		
		//方法1：调用DecimalFormat类来为数字保留后两位。
		//DecimalFormat df = new DecimalFormat("#.##");
		//System.out.println("保留小数点后两位"+"面积为："+df.format(area)+"周长为："+df.format(perimeter));
	
		//方法2：BigDecimal来保留后两位小数。
		BigDecimal bd_area = new BigDecimal(area);
		BigDecimal bd_perimeter = new BigDecimal(perimeter);
		bd_area = bd_area.setScale(2, BigDecimal.ROUND_HALF_UP);
		bd_perimeter = bd_perimeter.setScale(2, BigDecimal.ROUND_HALF_UP);
		System.out.println("保留小数点位数"+"面积为："+bd_area+"周长为："+bd_perimeter);
	}

}
