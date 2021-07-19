#include <bits/stdc++.h>
using namespace std;

int main() {
	//part a - x0 = 0.2
	//part b - x0 = -0.001
	//part c - x0 = 0.999
	//part d - x0 = 1.2
	//part e - x0 = 1.801
	float x0 = 1.801; // change this value!
	for (int i = 0; i < 5000; i++) {
		float curr = x0 + (1.25 * (1 - x0)) * x0;
		cout << curr << endl;
		x0 = curr;
	}
}
