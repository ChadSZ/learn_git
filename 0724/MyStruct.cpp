#include<iostream>
#include<string>
using namespace std;

struct SummerTrainning{
	string name;
	string sex;
	char num[20];
	string address;
};

int main(){
	SummerTrainning S{
		"shenzhang",
		"male",
		"P19301146",
		"��԰"
	};

	cout << "������" << S.name << endl;
	cout << "�Ա�" << S.sex << endl;
	cout << "ѧ�ţ�" << S.num << endl;
	cout << "��ַ��" << S.address << endl;

	int test;
	cout << "����please:" << endl;
	cin >> test;
	system("pause");

	return 0;
}