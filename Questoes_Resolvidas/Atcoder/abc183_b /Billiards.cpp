#include <bits/stdc++.h>

using namespace std;

int main() {
    double Sx, Sy, Gx, Gy;

    cin >> Sx >> Sy >> Gx >> Gy;

    double targetX = (Gx * Sy + Sx * Gy) / (Sy + Gy);

    cout << fixed << setprecision(10) << targetX << endl;

    return 0;
}

// Adicionar imagem e fórmula na versão final