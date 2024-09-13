from typing import List
from math import hypot, acos, fabs, sin, tan, pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Polygon:
    def __init__(self, ps: List[Point]):
        self.vs = ps
        self.n = len(self.vs)
        self.vs.append(self.vs[0])

    def _D(self, P: Point, Q: Point, R: Point):
        return (P.x * Q.y + P.y * R.x + Q.x * R.y) - (R.x * Q.y + R.y * P.x + Q.x * P.y)

    def convex(self):
        if self.n < 3:
            return False

        P = 0
        N = 0
        Z = 0

        for i in range(self.n):
            d = self._D(self.vs[i], self.vs[(i + 1) % self.n], self.vs[(i + 2) % self.n])
            if d:
                if d > 0:
                    P += 1
                else:
                    N += 1
            else:
                Z += 1

        return P == self.n or N == self.n

    def _distance(self, P: Point, Q: Point):
        return hypot(P.x - Q.x, P.y - Q.y)

    def perimeter(self):
        p = 0.0

        for i in range(self.n):
            p += self._distance(self.vs[i], self.vs[i + 1])

        return p

    def area(self):
        a = 0.0

        for i in range(self.n):
            a += self.vs[i].x * self.vs[i + 1].y
            a -= self.vs[i + 1].x * self.vs[i].y

        return 0.5 * fabs(a)

    def _angle(self, P: Point, A: Point, B: Point):
        ux = P.x - A.x
        uy = P.y - A.y

        vx = P.x - B.x
        vy = P.y - B.y

        num = ux * vx + uy * vy
        den = hypot(ux, uy) * hypot(vx, vy)

        return acos(num / den)

    def _equals(self, x: float, y: float):
        EPS = 1e-6
        return fabs(x - y) < EPS

    def contains(self, P: Point):
        if self.n < 3:
            return False

        sum = 0.0

        for i in range(self.n):
            d = self._D(P, self.vs[i], self.vs[i + 1])
            a = self._angle(P, self.vs[i], self.vs[i + 1])
            sum += a if d > 0 else (-a if d < 0 else 0)

        return self._equals(fabs(sum), 2 * pi)
    
    def contains2(self, point: Point) -> bool:
        n = len(self.vs)
        dentro = False

        p = point
        for i in range(n):
            q = self.vs[i]
            r = self.vs[(i + 1) % n]

            # Verifique se o ponto está exatamente sobre uma aresta
            if (q.y == p.y and r.y == p.y and q.x <= p.x <= r.x) or (
                r.x <= p.x <= q.x and r.y == p.y and q.y == p.y
            ):
                return True

            if (q.y <= p.y < r.y or r.y <= p.y < q.y) and p.x < (
                (r.x - q.x) * (p.y - q.y) / (r.y - q.y) + q.x
            ):
                dentro = not dentro

        return dentro

    def _cross_product(self, p1: Point, p2: Point, p3: Point) -> float:
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    def contains_cross_product(self, point: Point) -> bool:
        for i in range(self.n):
            cross_product = self._cross_product(self.vs[i], self.vs[i + 1], point)
            if cross_product < 0:  # Ponto está à direita da aresta
                return False
            elif cross_product == 0:  # Ponto está sobre a aresta
                return True

        return True  # Ponto está dentro do polígono

    def _intersection(self, P: Point, Q: Point, A: Point, B: Point):
        a = B.y - A.y
        b = A.x - B.x
        c = B.x * A.y - A.x * B.y
        u = fabs(a * P.x + b * P.y + c)
        v = fabs(a * Q.x + b * Q.y + c)

        return Point((P.x * v + Q.x * u) / (u + v), (P.y * v + Q.y * u) / (u + v))

    def cut_polygon(self, A: Point, B: Point):
        points = []
        EPS = 1e-6

        for i in range(self.n):
            d1 = self._D(A, B, self.vs[i])
            d2 = self._D(A, B, self.vs[i + 1])

            if d1 > -EPS:
                points.append(self.vs[i])

            if d1 * d2 < -EPS:
                points.append(self._intersection(self.vs[i], self.vs[i + 1], A, B))

        return Polygon(points)

    def circumradius(self):
        s = self._distance(self.vs[0], self.vs[1])

        return (s / 2.0) * (1.0 / sin(pi / self.n))

    def apothem(self):
        s = self._distance(self.vs[0], self.vs[1])

        return (s / 2.0) * (1.0 / tan(pi / self.n))
    from math import hypot, acos

    def segment_angles(P, Q, R, S):
        ux = P.x - Q.x
        uy = P.y - Q.y

        vx = R.x - S.x
        vy = R.y - S.y

        num = ux * vx + uy * vy
        den = hypot(ux, uy) * hypot(vx, vy)

        # Caso especial: se den == 0, algum dos vetores é degenerado
        if den == 0:
            return None

        return acos(num / den)



N, Q = map(int, input().split())

vertices = []
coords = list(map(int, input().split()))
for i in range(0, 2 * N, 2):
    vertices.append(Point(coords[i], coords[i + 1]))

polygon = Polygon(vertices)

for _ in range(Q):
    x, y = map(int, input().split())
    if polygon.contains_cross_product(Point(x, y)):
        print("D")
    else:
        print("F")