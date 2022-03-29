#include <bits/stdc++.h>
using namespace std;
int main() {
	float x = (float) -80/81; //change the value of x here. Enter in fraction or decimal form and don't forget the semicolon at the end! Click run to see the converging value.
	float sum = 1.0;
	for (int i = 1; i <= 1000; i++) {
		sum += pow(x, i);
	}
	cout << sum << endl;
}
