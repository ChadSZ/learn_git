package area_perimeter;

import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.util.zip.CRC32;

public class Cylinder extends Circle{
	private double hight;
	private double radius;
	public Cylinder() {
		super();
		
	}
	public Cylinder(double hight) {
		super();
		this.hight = hight;
	}
	public double getHight() {
		return hight;
	}
	public void setHight(double hight) {
		this.hight = hight;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Circle cylinder = new Cylinder();
		cylinder.ScannerTest();	
	}

}
