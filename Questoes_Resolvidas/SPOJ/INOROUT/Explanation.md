## INOROUT - Inside or outside?

**Juiz Online:** SPOJ - [https://www.spoj.com/problems/INOROUT/](https://www.spoj.com/problems/INOROUT/)

**Linguagem:** Python

## Descrição:

Dado um polígono convexo de N vértices, em ordem anti-horária, e Q consultas, cada consulta representando um ponto no plano cartesiano, determine se cada ponto está dentro ou fora do polígono.

## Solução:

**Explicação:**

Utilizamos a classe `Polygon` (a explicação completa do código da classe `Polygon` está disponível em `Polygon.md`) e duas de suas funções para resolver este problema:

1. **`contains_cross_product`:** Esta função utiliza o produto vetorial para determinar se um ponto está dentro do polígono.
   - Para cada aresta do polígono, calculamos o produto vetorial entre o vetor formado pela aresta e o vetor formado pelo primeiro ponto da aresta e o ponto de consulta.
   - Se o produto vetorial for negativo, o ponto está à direita da aresta e, portanto, fora do polígono.
   - Se o produto vetorial for zero, o ponto está sobre a aresta e é considerado dentro do polígono.
   - Se o produto vetorial for positivo para todas as arestas, o ponto está dentro do polígono.

2. **`_cross_product`:** Esta função auxiliar calcula o produto vetorial entre dois vetores.

**Código:**

```python
# ... (código da classe Polygon em Polygon.md)

N, Q = map(int, input().split())

vertices = []
coords = list(map(int, input().split()))
for i in range(0, 2 * N, 2):
    vertices.append(Point(coords[i], coords[i + 1]))

polygon = Polygon(vertices)

for _ in range(Q):
    x, y = map(int, input().split())
    if polygon.contains_cross_product(Point(x, y)):
        print("D")  # Dentro
    else:
        print("F")  # Fora
```

## Complexidade:

* **Construção do polígono:** A leitura dos vértices e criação do polígono tem complexidade **O(N)**.
* **Processamento das consultas:** Para cada consulta, a função `contains_cross_product` itera por todas as arestas do polígono, resultando em uma complexidade **O(N)** por consulta.

Portanto, a complexidade de tempo total da solução é **O(N + Q * N)**, que pode ser simplificada para **O(Q * N)**, considerando que Q (o número de consultas) é geralmente maior que N (o número de vértices).
