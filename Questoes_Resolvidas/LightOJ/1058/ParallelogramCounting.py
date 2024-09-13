from typing import List
from collections import defaultdict

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def count_parallelograms(points: List[Point]) -> int:
    n = len(points)
    midpoint_counts = defaultdict(int)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Calcula o ponto médio da diagonal
            mid_x = (points[i].x + points[j].x) 
            mid_y = (points[i].y + points[j].y) 

            # Utiliza o ponto médio como chave do dicionário (representando a diagonal)
            midpoint_counts[(mid_x, mid_y)] += 1

    # Para cada ponto médio (diagonal) com contagem > 1, calcula as combinações
    for value in midpoint_counts.values():
        if value > 1:
            count += value * (value - 1) // 2  # Combinações de 2

    return count


T = int(input())

for case in range(1, T + 1):
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))

    print(f"Case {case}: {count_parallelograms(points)}")