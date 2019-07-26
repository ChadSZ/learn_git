#include<iostream>
#include<fstream>
using namespace std;
int main(){
	for (int x = 1; x < 10; x++){
		for (int y = 1; y <= x; y++){
			cout << y << "*" << x << "=" << x*y<<"\t";
		}
		cout << endl;
	}
	return 0;
}