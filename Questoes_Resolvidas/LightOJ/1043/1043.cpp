#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        double AB, AC, BC, ratio;
        cin >> AB >> AC >> BC >> ratio;

        double s = (AB + AC + BC) / 2.0;
        double areaABC = sqrt(s * (s - AB) * (s - AC) * (s - BC));

        double areaADE = areaABC * ratio / (ratio + 1);

        // Brincadeira de Ensino médio
        double AD = AB * sqrt(areaADE / areaABC);

        cout << fixed << setprecision(10) << "Case " << i << ": " << AD << endl;
    }

    return 0;
}