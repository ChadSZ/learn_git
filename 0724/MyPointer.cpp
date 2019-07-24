/*C++pointer功能*/
#include<iostream>
using namespace std;
int main(){
	int a = 'a';
	int *data = &a;
	cout << "变量data的值：" << data << "*data的值:" << *data << endl;
	int **pt = &data;
	cout <<"**pt的值："<<**pt<< "*pt的值:" << *pt << " pt的值:" << pt << endl;

}