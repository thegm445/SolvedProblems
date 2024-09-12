import matplotlib.pyplot as plt

def plot_triangle_on_rectangle(w, h, points):
  """
  Plota o retângulo, os pontos e o triângulo de área máxima.

  Args:
    w: Largura do retângulo.
    h: Altura do retângulo.
    points: Lista de tuplas (x, y) representando os pontos nas bordas.
  """

  fig, ax = plt.subplots()

  # Desenhar retângulo
  rectangle = plt.Rectangle((0, 0), w, h, edgecolor='black', facecolor='none', linewidth=2)
  ax.add_patch(rectangle)

  # Desenhar pontos
  for x, y in points:
    plt.plot(x, y, marker='o', markersize=5, color='blue')

  # Encontrar e desenhar triângulo de área máxima (apenas para ilustração)
  max_area = 0
  triangle_points = None
  for i in range(len(points)):
    for j in range(i+1, len(points)):
      for k in range(j+1, len(points)):
        # Verificar se exatamente dois pontos estão no mesmo lado
        if (points[i][0] == points[j][0] and points[i][1] != points[k][1]) or \
           (points[i][1] == points[j][1] and points[i][0] != points[k][0]) or \
           (points[i][0] == points[k][0] and points[i][1] != points[j][1]) or \
           (points[i][1] == points[k][1] and points[i][0] != points[j][0]):
          area = 0.5 * abs((points[j][0] - points[i][0]) * (points[k][1] - points[i][1]) - 
                           (points[k][0] - points[i][0]) * (points[j][1] - points[i][1]))
          if area > max_area:
            max_area = area
            triangle_points = [points[i], points[j], points[k]]

  if triangle_points:
    triangle = plt.Polygon(triangle_points, edgecolor='red', facecolor='none', linewidth=2)
    ax.add_patch(triangle)

  # Configurar gráfico
  plt.xlim(-1, w+1)
  plt.ylim(-1, h+1)
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('Triângulo de Área Máxima em um Retângulo')
  plt.grid(True)
  plt.savefig("Example1.png")

# Exemplo de entrada
w = 5
h = 8
points = [(1, 0), (2, 0), (2, 8), (3, 8), (0, 1), (0, 4), (5, 4), (5, 6)]

# Plotar gráfico
plot_triangle_on_rectangle(w, h, points)