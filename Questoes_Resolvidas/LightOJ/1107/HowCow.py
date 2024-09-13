from math import hypot, acos, sin, tan, pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Polygon:
    def __init__(self, points):
        self.points = points
        self.n = len(points)+1
        # Primeiro ponto ao final.
        self.points.append(self.points[0])

    def _D(self, P: Point, Q: Point, R: Point):
        # É o D do positivo ou negativo.
        return (P.x * Q.y + P.y * R.x + Q.x * R.y) - (R.x * Q.y + R.y * P.x + Q.x * P.y)

    def _convex(self):
        # É convexo? (código reescrito do github)
        if self.n < 3: 
            return False

        P, N, Z = 0, 0, 0
        for i in range(self.n):
            d = self._D(self.points[i], self.points[i + 1], self.points[(i + 2) % self.n])
            if d > 0: 
                P += 1
            elif d < 0: 
                N += 1
            else: 
                Z += 1
        return P == self.n or N == self.n

    def _perimeter(self):
        # Loucuras de python.
        return sum(hypot(self.points[i].x - self.points[i + 1].x, 
                         self.points[i].y - self.points[i + 1].y) for i in range(self.n) )

    def _area(self):
        # Loucuras de python parte 2
        a = sum(self.points[i].x * self.points[i + 1].y - 
                self.points[i + 1].x * self.points[i].y 
                for i in range(self.n))
        return 0.5 * abs(a)

    def _angle(self, P, A, B):
        # Qual o ângulo entre as linhas?
        ux, uy = P.x - A.x, P.y - A.y
        vx, vy = P.x - B.x, P.y - B.y
        num = ux * vx + uy * vy
        den = hypot(ux, uy) * hypot(vx, vy)
        return acos(num / den) if den else 0  # Trata caso de vetor degenerado

    def _contains(self, P: Point) -> bool:  # ALGO DE ERRADO, VERIFICAR O QUE
        # Um ponto está dentro ou fora da área?
        if self.n < 3: 
            return False

        sum_angles = 0
        for i in range(0,self.n - 1):
            d = self._D(P, self.points[i], self.points[i + 1])
            a = self._angle(P, self.points[i], self.points[i + 1])
            sum_angles += a if d > 0 else (-a if d < 0 else 0)

        return bool(abs(sum_angles - 2 * pi) < 1e-6)  # Tolerância para comparação de floats

    def _intersection(self, P: Point, Q: Point, A: Point, B: Point):
        # Onde as linhas se cruzam?
        a = B.y - A.y
        b = A.x - B.x
        c = B.x * A.y - A.x * B.y
        u = abs(a * P.x + b * P.y + c)
        v = abs(a * Q.x + b * Q.y + c)
        return Point((P.x * v + Q.x * u) / (u + v), (P.y * v + Q.y * u) / (u + v))

    def _cut_polygon(self, A, B):
        # Como dividir a área com uma linha?
        new_points = []
        for i in range(self.n):
            d1 = self._D(A, B, self.points[i])
            d2 = self._D(A, B, self.points[i + 1])

            if d1 > -1e-6:  # Vértice à esquerda da reta
                new_points.append(self.points[i])

            if d1 * d2 < -1e-6:  # A aresta cruza a reta
                new_points.append(self._intersection(self.points[i], self.points[i + 1], A, B))

        return Polygon(new_points)

    def _circumradius(self):
        # Qual o tamanho da roda gigante que cabe em volta?
        if self.n < 3:
            return 0  # Não definido para polígonos com menos de 3 lados
        s = hypot(self.points[1].x - self.points[0].x, self.points[1].y - self.points[0].y)
        return (s / 2.0) * (1.0 / sin(pi / self.n))

    def _apothem(self):
        # aQual a distância do centro até o meio de um lado (se for um polígono regular)?
        if self.n < 3:
            return 0  # Não definido para polígonos com menos de 3 lados
        s = hypot(self.points[1].x - self.points[0].x, self.points[1].y - self.points[0].y)
        return (s / 2.0) * (1.0 / tan(pi / self.n))



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
