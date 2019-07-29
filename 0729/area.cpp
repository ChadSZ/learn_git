#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;
#define PI 3.14;

void triangle(){
	double a, b, c;
	cout << "请输入三角形的三边" << endl;
	
	cin >> a >> b >> c;
	
	if (a > 0 && b > 0 && c > 0){
		if (((a + b) > c) && ((a + c) > b) && ((b + c) > a)){
			double p = a + b + c;
			double s = (p*(p - a)*(p - b)*(p - c));
			cout << "三角形面积为：" << setiosflags(ios::fixed) << setprecision(2) << s << endl;
		}
		else
			cout << "数据不满足三角形构成原则" << endl;
	}
	else
		cout << "三角形的边不全大于0" << endl;
	
}

void rectangle(){
	double a,b;
	cout << "请输入矩形的两边：" << endl;
	cin >> a >> b;
	if (a > 0 && b > 0){
		double s = a*b;
		cout << "矩形面积为：" << setiosflags(ios::fixed) << setprecision(2) << s << endl;
	}
	else{
		cout << "矩形的两边输入错误" << endl;
	}
	
}

void circle(){
	double r;
	cout << "请输入圆形的半径：" << endl;
	cin >> r;
	if (r > 0){
	double s = r*r*PI;
	cout << "矩形面积为：" << setiosflags(ios::fixed) << setprecision(2) << s << endl;
	}
	else{
		cout << "圆的半径输入错误" << endl;
	}
}

void main(){

	int i;
	cout << "请输入一下数字代表计算不同的图形面积："  << endl;
	cout << "1：三角形，2：矩形，3：圆形" << endl;
	cout << "请选择图形：";
	cin >> i;
	switch (i)
	{
	case 1:	
		triangle();
		break;
	case 2:
		rectangle();
		break;
	case 3:
		circle();
		break;
	default:
		cout << "没有这种图形" << endl;
	}
}
