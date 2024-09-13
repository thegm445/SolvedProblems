## Leaping Tak

**Juiz Online:** AtCoder - [https://atcoder.jp/contests/abc179/tasks/abc179_d](https://atcoder.jp/contests/abc179/tasks/abc179_d)

**Linguagem:** C++

## Descrição:

Takahashi está na célula 1 de um conjunto de N células dispostas em linha e quer chegar à célula N. Ele pode se mover de uma célula `i` para uma célula `i + d`, onde `d` pertence a um conjunto S formado pela união de K segmentos não sobrepostos [L1, R1], [L2, R2], ..., [Lk, Rk]. Encontre o número de maneiras possíveis de Takahashi chegar à célula N, módulo 998244353.

## Solução:

**Explicação:**

A solução utiliza programação dinâmica para calcular o número de maneiras de chegar a cada célula.

1. **DP Array:**
   - Criamos um array `dp` de tamanho N + 1, onde `dp[i]` representa o número de maneiras de chegar à célula `i`.

2. **Inicialização:**
   - `dp[1] = 1`, pois há apenas uma maneira de começar na célula 1.

3. **Iteração:**
   - Para cada célula `i` de 2 a N:
     - Para cada segmento `[L, R]`:
       - Se `i - R` está dentro dos limites (maior ou igual a 1) e `i - L` é maior ou igual a `i - R`, significa que podemos alcançar a célula `i` a partir de uma célula no intervalo `[i - R, i - L]` usando um salto do segmento `[L, R]`.
       - Somamos o número de maneiras de chegar às células nesse intervalo ao valor de `dp[i]`.

4. **Soma de prefixos:**
   - Utilizamos um array `prefix_sum` para armazenar a soma dos prefixos do array `dp`. Isso permite calcular a soma de um intervalo de `dp` em tempo constante.

5. **Módulo:**
   - Em cada etapa, calculamos os valores módulo 998244353 para evitar overflow.

**Código:**

```c++
#include <bits/stdc++.h>
using namespace std;

#define MOD 998244353
#define ii pair<int,int>

int main() {
    int N, K;
    cin >> N >> K;

    vector<ii> segments(K);
    for (int i = 0; i < K; i++) {
        cin >> segments[i].first >> segments[i].second; 
    }

    vector<long long> dp(N + 1, 0);
    vector<long long> prefix_sum(N + 1, 0); 

    dp[1] = 1;
    prefix_sum[1] = 1;

    for (int i = 2; i <= N; ++i) {
        for (int j = 0; j < K; ++j) {
            int L = segments[j].first;
            int R = segments[j].second;
            int start = max(1, i - R);
            int end = i - L;

            if (end >= start) {
                dp[i] = (dp[i] + prefix_sum[end] - (start > 1 ? prefix_sum[start - 1] : 0)) % MOD;
                if (dp[i] < 0) dp[i] += MOD;  // Ajustar para o caso de valores negativos
            }
        }
        prefix_sum[i] = (prefix_sum[i - 1] + dp[i]) % MOD;
    }

    cout << dp[N] << endl;
    return 0;
}
```

## Complexidade:

* **Iteração:** A iteração pelas células e pelos segmentos tem complexidade **O(N * K)**.
* **Soma de prefixos:** A atualização do array `prefix_sum` tem complexidade **O(N)**.

Portanto, a complexidade de tempo total da solução é **O(N * K)**.
