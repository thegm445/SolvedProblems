## How Cow

**Juiz Online:** LightOJ - [https://lightoj.com/problem/how-cow](https://lightoj.com/problem/how-cow)

**Linguagem:** Python

## Descrição:

Dado um terreno retangular representado por suas coordenadas inferior esquerda (x1, y1) e superior direita (x2, y2), e um conjunto de M vacas representadas por suas coordenadas (x, y), determine se cada vaca está dentro ou fora do terreno.

## Solução:

**Explicação:**

A solução utiliza a classe `Polygon` (a explicação completa do código da classe `Polygon` está disponível em `Polygon.md`) para representar o terreno retangular e a função `_contains` para verificar se cada vaca está dentro do polígono.

1. **Criar o polígono:** Criamos uma instância da classe `Polygon` com as coordenadas dos vértices do retângulo.
2. **Verificar se as vacas estão dentro:** Para cada vaca, criamos um ponto com suas coordenadas e usamos a função `_contains` para verificar se o ponto está dentro do polígono. (tive que adicionar um na contagem de pontos, bem como adicionar o ponto inicial no final do array dos pontos).

**Código:**

```python
# ... (código da classe Polygon em Polygon.md)

t = int(input())
for case in range(1, t + 1):
    x1, y1, x2, y2 = map(int, input().split())
    m = int(input())
    land = Polygon([Point(x1, y1), Point(x2, y1), Point(x2, y2), Point(x1, y2)])

    print(f"Case {case}:")
    for _ in range(m):
        x, y = map(int, input().split())
        cow = Point(x, y)
        print("Yes" if land._contains(cow) else "No")
```

**Complexidade:**

A complexidade de tempo da solução é **O(M)**, onde M é o número de vacas, pois iteramos por cada vaca uma vez para verificar se está dentro do polígono. A função `_contains` tem complexidade **O(N)**, onde N é o número de lados do polígono (4 no caso do retângulo), mas como N é constante neste problema, a complexidade total permanece **O(M)**.