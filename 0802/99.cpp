#include<iostream>
using namespace std;
int main()
{
	int i, j;

	for (i = 1; i <= 9; i++){
		for (j = 1; j <= i; j++){
			cout << j << '*' << i <<'='<< j*i << '\t';
			//cout << '*';
		}
		cout << endl;
	}
	return 0;
}