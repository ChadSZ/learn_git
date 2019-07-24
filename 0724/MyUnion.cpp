/*union¹²ÓÃÌå*/
#include<iostream>
using namespace std;
int main(){
	union{
		long a;
		char b;
		float c;
	}un;
	/*
	un.b = 'a';
	cout << "char:" << un.b << endl;
	un.a = 'a';
	cout << "int:" <<un.a<<endl;
	*/
	/*
	un.a = 'a';
	cout <<un.a<<endl;
	cout << un.b<< endl;
	cout << un.c << endl;
	*/
	/*
	un.a = 'b';
	cout << un.a << endl;
	cout << un.b << endl;
	cout << un.c << endl;
	*/
	un.a = 1;
	cout << un.a << endl;
	cout << un.b << endl;
	cout << un.c << endl;
	un.b = 'c';
	cout << un.a << endl;
	cout << un.b << endl;
	cout << un.c << endl;
	un.c = 10.0;
	cout << un.a << endl;
	cout << un.b << endl;
	cout << un.c << endl;
}