/*C++pointer����*/
#include<iostream>
using namespace std;
int main(){
	int a = 'a';
	int *data = &a;
	cout << "����data��ֵ��" << data << "*data��ֵ:" << *data << endl;
	int **pt = &data;
	cout <<"**pt��ֵ��"<<**pt<< "*pt��ֵ:" << *pt << " pt��ֵ:" << pt << endl;

}