#include <bits/stdc++.h>
using namespace std;

int main() {
  float x0 = -10.00;
  for (int i = 0; i < 500; i++) {
	  float curr = sqrt(sqrt(1996 * x0));
	  cout << curr << endl;
	  x0 = curr;
  }
}
