/*类和对象， 求任意3点构成的三角形面积*/
//#ifndef _POINT_H
//#define _POINT_H
//
//#include <math.h>

//class Point
//{
//private:
//	float xCord, yCord;
//public:
//	Point() :xCord(0), yCord(0){} //利用无参数构建函数初始化 xCord 和 yCord
//	~Point();
//	Point(double, double);
//	double getxCord();
//	double getyCord();
//	//double getLenth();
//};
//class triangle{
//public:
//	double L; //第一条边长
//	double M; //第一条边长
//	double N; //第一条边长
//	// triangle() :L(0),M(0),N(0){}
//	triangle();
//	~triangle();
//	void getCord(Point u[]);
//	double getarea();
//	double getlength();
//
//};
//

//#endif


// Point.h

#ifndef _POINT_H
#define _POINT_H

#include <math.h>

class Point
{
private:
	float x, y;
public:
	Point(double a, double b){ x = a; y = b; }
	void print();
	friend double pointDistance(Point p1, Point p2);
	friend double area(Point p1, Point p2, Point p3);
};

#endif