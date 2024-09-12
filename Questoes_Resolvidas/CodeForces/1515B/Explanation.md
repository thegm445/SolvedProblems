## Phoenix and Puzzle

**Juiz Online:** Codeforces - [https://codeforces.com/problemset/problem/1515/B](https://codeforces.com/problemset/problem/1515/B)

**Linguagem:** C

## Descrição

Phoenix tem `n` peças de quebra-cabeça idênticas. Cada peça é um triângulo retângulo isósceles. O objetivo é formar um quadrado usando todas as `n` peças, sem sobreposição ou espaços vazios. Determine se é possível formar o quadrado com as peças dadas.

## Solução

**Explicação:**

A solução se baseia em duas observações principais:

1. **Quadrados a partir de triângulos:** Um quadrado pode ser formado com triângulos retângulos isósceles de duas maneiras:
   - **2 triângulos:** Formando um quadrado com a hipotenusa como diagonal.
   - **4 triângulos:** Formando um quadrado com os catetos como lados.

2. **Número de peças:** Para formar um quadrado com as peças dadas, o número total de peças (`n`) deve ser:
   - **Múltiplo de 2:** Se usarmos a configuração de 2 triângulos por quadrado.
   - **Múltiplo de 4:** Se usarmos a configuração de 4 triângulos por quadrado.

**Imagem:**

#### This is the piece
![image](PuzzlePiece.png)

#### Two Pieces
![image](n2Square.png)

#### Four Pieces
![image](n4Square.png)

**Verificação:**

1. **Verificar se 'n' é múltiplo de 2:** Se `n` não for divisível por 2, não é possível formar um quadrado.
2. **Verificar raiz quadrada:**
   - Se `n` for divisível por 2, calcular a raiz quadrada de (`n / 2`). Se a raiz quadrada for um número inteiro, significa que podemos formar um quadrado usando a configuração de 2 triângulos.
   - Se `n` for divisível por 4, calcular a raiz quadrada de (`n / 4`). Se a raiz quadrada for um número inteiro, significa que podemos formar um quadrado usando a configuração de 4 triângulos.

```c
#include <stdio.h>
#include <math.h>
int main(){
    int t; scanf("%d",&t);
    while(t--){
        int n; scanf("%d",&n);
 
        int o_do_dois = sqrt(n/2); 
        int o_do_quatro = sqrt(n/4); 
 
        if( (n%2==0) && ( o_do_dois*o_do_dois == n/2 ) ){
            printf("YES\n");
        }
        else if( (n%4==0) && (o_do_quatro*o_do_quatro) == n/4 ){
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }
}
```

## Complexidade

A complexidade de tempo da solução é **O(1)**, pois realizamos um número constante de operações para cada caso de teste, independentemente do valor de `n`.