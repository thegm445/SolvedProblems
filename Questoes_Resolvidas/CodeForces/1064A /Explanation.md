## Make a triangle!

**Juiz Online:** Codeforces - [https://codeforces.com/problemset/problem/1064/A](https://codeforces.com/problemset/problem/1064/A)

**Linguagem:** C

## Descrição

Dado três segmentos de reta com comprimentos a, b e c, determine o número mínimo de minutos necessários para formar um triângulo de área positiva aumentando o comprimento de um segmento em 1 centímetro por minuto.

## Solução

**Explicação:**

A solução se baseia na desigualdade triangular: a soma dos comprimentos de quaisquer dois lados de um triângulo deve ser maior que o comprimento do terceiro lado.

1. **Ordenar os segmentos:** Ordene os segmentos em ordem crescente de comprimento (a <= b <= c).
2. **Verificar a desigualdade triangular:** Se a soma dos dois menores lados (a + b) já é maior que o maior lado (c), então um triângulo já pode ser formado (minutos = 0).
3. **Calcular os minutos necessários:** Caso contrário, precisamos aumentar o comprimento do menor lado (a) até que a desigualdade triangular seja satisfeita. O número mínimo de minutos será (c - a - b + 1).

```c
#include <stdio.h>

#define max(A, B) (A > B ? A : B)
#define swap(A, B) { int temp = A; A = B; B = temp; }

int main() {
    int a, b, c;
    scanf("%d %d %d", &a,&b,&c);

    // Ordenar os segmentos
    if (a > b) swap(a, b);
    if (b > c) swap(b, c);
    if (a > b) swap(a, b); 

    int minutes = max(0, c - a - b + 1);

    printf("%d\n",minutes);
    return 0;
}
```

## Complexidade

A complexidade de tempo da solução é **O(1)**, pois realizamos um número constante de operações para ordenar os segmentos e calcular o número de minutos. 