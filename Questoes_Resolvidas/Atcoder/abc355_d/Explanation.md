## Intersecting Intervals

**Juiz Online:** AtCoder - [https://atcoder.jp/contests/abc355/tasks/abc355_d](https://atcoder.jp/contests/abc355/tasks/abc355_d)

**Linguagem:** Python

## Descrição:

Dados N intervalos de números reais, onde o i-ésimo intervalo é representado por [li, ri], encontre o número de pares de intervalos (i, j), com 1 ≤ i < j ≤ N, que se intersectam.

## Solução:

**Explicação:**

A solução utiliza uma técnica chamada **"Sweep Line"** (Varredura de Linha) para contar as interseções de forma eficiente.

1. **Eventos:**
   - Criamos uma lista de eventos, onde cada evento representa o início ou o fim de um intervalo.
   - Cada evento é uma tupla `(ponto, tipo)`, onde:
     - `ponto`: o valor de `li` ou `ri`.
     - `tipo`: 0 para o início de um intervalo, 1 para o fim.

2. **Ordenar eventos:**
   - Ordenamos a lista de eventos em ordem crescente dos pontos. Em caso de empate, os eventos de início são considerados menores que os eventos de fim (para garantir que um intervalo seja contado como "ativo" antes de seu ponto final ser encontrado).

3. **Varredura:**
   - Percorremos a lista de eventos ordenada, mantendo um contador `gremio` que representa o número de intervalos ativos naquele momento.
   - Para cada evento:
     - Se for um evento de início (`tipo == 0`):
       - Incrementamos `gremio`.
       - Adicionamos `gremio` ao contador de interseções `inter`, pois o novo intervalo intersecta com todos os `gremio` intervalos que já estavam ativos.
     - Se for um evento de fim (`tipo == 1`):
       - Decrementamos `gremio`, pois um intervalo se tornou inativo.

4. **Resultado:**
   - Após processar todos os eventos, `inter` conterá o número total de pares de intervalos que se intersectam.

**Código:**

```python
N = int(input())
v = [tuple(map(int,input().split())) for _ in range(0,N)]
balela = []

for i in range(0,N):
    balela.append((v[i][0],0))
    balela.append((v[i][1],1))

balela.sort()

inter = 0
gremio = 0

for point, event_type in balela:
    if event_type == 0:
        inter += gremio
        gremio += 1
    else: 
        gremio -= 1 

print(inter)
```

## Complexidade:

* **Ordenação:** A ordenação dos eventos tem complexidade **O(N log N)**, onde N é o número de intervalos.
* **Varredura:** A varredura dos eventos tem complexidade **O(N)**.

Portanto, a complexidade de tempo total da solução é **O(N log N)**, dominada pela etapa de ordenação.
