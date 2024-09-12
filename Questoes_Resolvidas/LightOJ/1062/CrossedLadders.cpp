#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    double x, y, c;
    cin >> x >> y >> c;

    double left = 0, right = min(x, y);
    for (int i = 0; i < 100; i++) {
      double mid = (left + right) / 2;

      double h1 = sqrt(x * x - mid * mid);
      double h2 = sqrt(y * y - mid * mid);

      if (h1 * h2 / (h1 + h2) < c) {
        right = mid;
      } else {
        left = mid;
      }
    }
    cout << fixed << setprecision(6) << "Case " << t << ": " << left << endl;
  }

  return 0;
}