#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;
#define PI 3.14;

void triangle(){
	double a, b, c;
	cout << "�����������ε�����" << endl;
	
	cin >> a >> b >> c;
	
	if (a > 0 && b > 0 && c > 0){
		if (((a + b) > c) && ((a + c) > b) && ((b + c) > a)){
			double p = a + b + c;
			double s = (p*(p - a)*(p - b)*(p - c));
			cout << "���������Ϊ��" << setiosflags(ios::fixed) << setprecision(2) << s << endl;
		}
		else
			cout << "���ݲ����������ι���ԭ��" << endl;
	}
	else
		cout << "�����εı߲�ȫ����0" << endl;
	
}

void rectangle(){
	double a,b;
	cout << "��������ε����ߣ�" << endl;
	cin >> a >> b;
	if (a > 0 && b > 0){
		double s = a*b;
		cout << "�������Ϊ��" << setiosflags(ios::fixed) << setprecision(2) << s << endl;
	}
	else{
		cout << "���ε������������" << endl;
	}
	
}

void circle(){
	double r;
	cout << "������Բ�εİ뾶��" << endl;
	cin >> r;
	if (r > 0){
	double s = r*r*PI;
	cout << "�������Ϊ��" << setiosflags(ios::fixed) << setprecision(2) << s << endl;
	}
	else{
		cout << "Բ�İ뾶�������" << endl;
	}
}

void main(){

	int i;
	cout << "������һ�����ִ�����㲻ͬ��ͼ�������"  << endl;
	cout << "1�������Σ�2�����Σ�3��Բ��" << endl;
	cout << "��ѡ��ͼ�Σ�";
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
		cout << "û������ͼ��" << endl;
	}
}
