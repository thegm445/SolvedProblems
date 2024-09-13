## Sum Of Angles

**Juiz Online:** AtCoder - [https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_a](https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_a)

**Linguagem:** C

## Descrição:

Dado um inteiro N, representando o número de lados de um polígono regular convexo, calcule a soma dos ângulos internos do polígono, em graus.

## Solução:

**Fórmula:**

```
Soma dos ângulos internos = (N - 2) * 180°
```

**Explicação:**

1. **Triangulação:**  Um polígono convexo com N lados pode ser dividido em (N - 2) triângulos.

2. **Soma dos ângulos de um triângulo:** A soma dos ângulos internos de qualquer triângulo é sempre 180°.

3. **Soma total:** Como o polígono é dividido em (N - 2) triângulos, a soma total dos ângulos internos do polígono será `(N - 2) * 180°`.

**Código:**

```c
#include <stdio.h>


int main(){
    // ... (código com array pré-computado para 3 <= N <= 100)

    int n = 0; scanf("%d",&n);

    printf("%d\n",v[n-3]);
}
```

**Observação:** O código utiliza um array pré-computado para armazenar a soma dos ângulos internos para cada valor de N entre 3 e 100, mas a fórmula `(N - 2) * 180°` poderia ser usada diretamente no código para calcular a resposta.

## Complexidade:

A complexidade de tempo da solução é **O(1)**, pois o acesso ao array pré-computado (ou o cálculo direto da fórmula) é uma operação de tempo constante.