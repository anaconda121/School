#include <bits/stdc++.h>

using namespace std;

int main() {
	float x = -1/3; // { -1 * sqrt(1/3) --> 1 * sqrt(1/3) } is the range of limiting values
	float ans = 1.0;
	for (long long i = 0; i < 100000; i++) {
		float new_term = 3 * pow(x, 2);
		ans += new_term;
		x = new_term;
	}
	cout << ans << endl;
	return 0;
}
