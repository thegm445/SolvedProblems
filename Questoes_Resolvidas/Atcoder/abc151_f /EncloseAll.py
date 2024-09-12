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