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
		"李园"
	};

	cout << "姓名：" << S.name << endl;
	cout << "性别：" << S.sex << endl;
	cout << "学号：" << S.num << endl;
	cout << "地址：" << S.address << endl;

	int test;
	cout << "输入please:" << endl;
	cin >> test;
	system("pause");

	return 0;
}