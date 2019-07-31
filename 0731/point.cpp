// Point.cpp

#include <iostream>
using namespace std;

#include "Point.h"

void Point::print()
{
	cout << "(" << x << "," << y << ")" << " ";
}

double pointDistance(Point p1, Point p2)
{
	double distance = 0;
	distance = sqrt((p1.y - p2.y)*(p1.y - p2.y) + (p1.x - p2.x)*(p1.x - p2.x));
	return distance;
}

double area(Point p1, Point p2, Point p3)
{
	double area = 0;
	double a = 0, b = 0, c = 0, s = 0;
	a = pointDistance(p1, p2);
	b = pointDistance(p2, p3);
	c = pointDistance(p1, p3);
	s = 0.5*(a + b + c);
	area = sqrt(s*(s - a)*(s - b)*(s - c));
	return area;
}
// PointMain.cpp

#include <iostream>
using namespace std;

#include "Point.h"

int main()
{
	double a, b;
	cout << "请输入第一个点的坐标：" << endl;
	cin >> a >> b ;
	Point p1(a, b);
	cout << "请输入第二个点的坐标：" << endl;
	cin >> a >> b;
	Point p2(a, b);
	cout << "请输入第三个点的坐标：" << endl;
	cin >> a >> b;
	Point p3(a, b);
	cout << "三角形顶点坐标为：";
	p1.print();
	p2.print();
	p3.print();
	cout << endl;
	cout << "三角形面积为：";
	cout << area(p1, p2, p3) << endl;
	return 0;
}
