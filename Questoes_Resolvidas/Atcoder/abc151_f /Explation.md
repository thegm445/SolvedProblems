## Enclose All

**Juiz Online:** AtCoder - [https://atcoder.jp/contests/abc151/tasks/abc151_f](https://atcoder.jp/contests/abc151/tasks/abc151_f)

**Linguagem:** Python

## Descrição

Dado um conjunto de N pontos em um plano cartesiano, encontre o menor raio possível de um círculo que englobe todos os pontos dentro ou na borda.

## Solução

A solução implementa o algoritmo de Welzl, um algoritmo recursivo para encontrar o menor círculo que engloba um conjunto de pontos.

**Pseudocódigo:**

```
função welzl(P, R, n):
  # P: conjunto de pontos
  # R: conjunto de pontos na borda do círculo
  # n: número de pontos em P

  # Caso base: nenhum ponto ou 3 pontos na borda
  se n == 0 ou tamanho(R) == 3:
    se tamanho(R) == 0:
      retorna ((0, 0), 0)  # Círculo degenerado
    senão se tamanho(R) == 1:
      retorna (R[0], 0)  # Círculo degenerado
    senão se tamanho(R) == 2:
      retorna (ponto médio de R[0] e R[1], distância entre R[0] e R[1] / 2)  # Círculo com diâmetro R[0]R[1]
    senão:
      retorna circulo_tres_pontos(R[0], R[1], R[2])  # Círculo definido pelos três pontos

  # Escolhe um ponto aleatório p de P
  p = elemento aleatório de P

  # Remove p de P
  P = P - {p}

  # Encontra o menor círculo D que engloba P - {p}
  D = welzl(P, R, n - 1)

  # Se p está dentro de D, então D também engloba P
  se distancia(p, centro de D) <= raio de D:
    retorna D

  # Caso contrário, p deve estar na borda do menor círculo que engloba P
  adiciona p a R

  # Encontra o menor círculo que engloba P, sabendo que p está na borda
  retorna welzl(P, R, n - 1)

função circulo_tres_pontos(p1, p2, p3):
  # Implementação para encontrar o círculo que passa por três pontos
  # ...
```

```python
import math, random


def distancia(p1, p2):
  return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))

# Função para calcular o círculo que passa por três pontos
def circulo_tres_pontos(p1, p2, p3):
  # Não pode dividir por 0, pontos colineares
  if (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) == 0:
    return None

  # Confia.
  x = (((p1[0]**2 + p1[1]**2) * (p2[1] - p3[1]) + (p2[0]**2 + p2[1]**2) * (p3[1] - p1[1]) + (p3[0]**2 + p3[1]**2) * (p1[1] - p2[1])) / (2 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))))
  y = (((p1[0]**2 + p1[1]**2) * (p3[0] - p2[0]) + (p2[0]**2 + p2[1]**2) * (p1[0] - p3[0]) + (p3[0]**2 + p3[1]**2) * (p2[0] - p1[0])) / (2 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))))
  r = distancia(p1, (x, y))
  return ((x, y), r)


def welzl_recursivo(pontos, pontos_borda, n):
  # Caso base: nenhum ponto ou 3 pontos na borda
  if n == 0 or len(pontos_borda) == 3:
    if len(pontos_borda) == 0:
      return ((0, 0), 0)
    elif len(pontos_borda) == 1:
      return (pontos_borda[0], 0)
    elif len(pontos_borda) == 2:
      return (((pontos_borda[0][0] + pontos_borda[1][0]) / 2, (pontos_borda[0][1] + pontos_borda[1][1]) / 2), distancia(pontos_borda[0], pontos_borda[1]) / 2)
    else:
      return circulo_tres_pontos(pontos_borda[0], pontos_borda[1], pontos_borda[2])

  # Escolhe um ponto aleatório e o remove do conjunto
  idx = random.randrange(n)
  p = pontos[idx]
  pontos[idx], pontos[n - 1] = pontos[n - 1], pontos[idx]

  # Calcula o círculo mínimo sem o ponto escolhidow
  c = welzl_recursivo(pontos, pontos_borda.copy(), n - 1)

  # Se o ponto está dentro do círculo, retorna o mesmo círculo
  if distancia(p, c[0]) <= c[1]:
    return c

  # Caso contrário, o ponto está na borda do círculo mínimo
  pontos_borda.append(p)
  return welzl_recursivo(pontos, pontos_borda.copy(), n - 1)

n = int(input())
pontos = [ list(map(int,input().split())) for i in range(0,n) ]

centro, raio = welzl_recursivo(pontos.copy(), [], len(pontos))

print(f"{raio:.7f}")
```

## Complexidade

A complexidade de tempo esperada do algoritmo de Welzl é O(N), onde N é o número de pontos. No entanto, a complexidade de tempo no pior caso é O(N!), mas isso é extremamente raro na prática devido à aleatoriedade na escolha do ponto p.