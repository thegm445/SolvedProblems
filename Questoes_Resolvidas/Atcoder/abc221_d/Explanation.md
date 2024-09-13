## Online Games

**Juiz Online:** AtCoder - [https://atcoder.jp/contests/abc221/tasks/abc221_d](https://atcoder.jp/contests/abc221/tasks/abc221_d)

**Linguagem:** C

## Descrição:

Há um jogo online com N jogadores registrados. O i-ésimo jogador fez login por Bi dias consecutivos, começando no dia Ai, e não fez login nos outros dias. Encontre o número de dias em que exatamente k jogadores fizeram login, para cada 1 ≤ k ≤ N.

## Solução:

**Explicação:**

A solução utiliza a técnica de "Sweep Line" para contar o número de jogadores que fizeram login em cada dia.

1. **Eventos:**
   - Criamos uma lista de eventos, onde cada evento representa o início ou o fim do período de login de um jogador.
   - Cada evento é uma estrutura `Event` com:
     - `day`: o dia do evento (Ai ou Ai + Bi).
     - `type`: 1 para início de login, -1 para fim de login.

2. **Ordenar eventos:**
   - Ordenamos a lista de eventos em ordem crescente dos dias. Em caso de empate, priorizamos eventos de fim de login sobre eventos de início de login (para evitar contabilizar um jogador duas vezes no mesmo dia).

3. **Varredura:**
   - Percorremos a lista de eventos ordenada, mantendo um contador `active_players` que representa o número de jogadores com login ativo naquele momento.
   - Para cada evento:
     - Se for um evento de início de login (`type == 1`):
       - Incrementamos `active_players`.
     - Se for um evento de fim de login (`type == -1`):
       - Decrementamos `active_players`.
     - Para cada dia entre o evento atual e o próximo, incrementamos o contador `days_with_k_players[active_players]`, que armazena o número de dias com exatamente `active_players` jogadores logados.

4. **Resultado:**
   - Após processar todos os eventos, o array `days_with_k_players` conterá o número de dias para cada valor de k.

**Código:**

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_EVENTS 400005

typedef struct Event {
    int day;
    int type; 
} Event;

// ... (código de ordenação mergesort)

int main() {
    int n;
    scanf("%d", &n);

    Event events[MAX_EVENTS];
    for (int i = 0; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        events[2 * i].day = a;
        events[2 * i].type = 1;
        events[2 * i + 1].day = a + b;
        events[2 * i + 1].type = -1; 
    }

    mergesort(events, 0, 2 * n - 1);

    int active_players = 0;
    int days_with_k_players[MAX_EVENTS] = {0};
    int prev_day = 0;

    for (int i = 0; i < 2 * n; i++) {
        days_with_k_players[active_players] += events[i].day - prev_day;
        active_players += events[i].type;
        prev_day = events[i].day;
    }

    for (int i = 1; i <= n; i++) {
        printf("%d ", days_with_k_players[i]);
    }
    printf("\n");

    return 0;
}
```

## Complexidade:

* **Ordenação:** A ordenação dos eventos tem complexidade **O(N log N)**, onde N é o número de jogadores.
* **Varredura:** A varredura dos eventos tem complexidade **O(N)**.

Portanto, a complexidade de tempo total da solução é **O(N log N)**, dominada pela etapa de ordenação.
