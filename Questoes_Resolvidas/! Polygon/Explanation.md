## Polygon.md

Este arquivo contém a explicação detalhada do código da classe `Polygon`, utilizada em diversas soluções de problemas de Geometria Computacional.

```python
from math import hypot, acos, fabs, sin, tan, pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Polygon:
    def __init__(self, ps: List[Point]):
        """
        Inicializa um polígono com uma lista de pontos.

        Args:
            ps: Lista de objetos Point representando os vértices do polígono em ordem anti-horária.
        """
        self.vs = ps
        self.n = len(self.vs)
        self.vs.append(self.vs[0])  # Adiciona o primeiro ponto ao final para facilitar cálculos cíclicos

    def _D(self, P: Point, Q: Point, R: Point):
        """
        Calcula o determinante da matriz 3x3 formada pelos pontos P, Q e R.
        Este valor é usado para determinar a orientação (horária, anti-horária ou colinear) de três pontos.

        Args:
            P: Primeiro ponto.
            Q: Segundo ponto.
            R: Terceiro ponto.

        Returns:
            float: O determinante da matriz. Um valor positivo indica orientação anti-horária, 
                   negativo indica horária e zero indica pontos colineares.
        """
        return (P.x * Q.y + P.y * R.x + Q.x * R.y) - (R.x * Q.y + R.y * P.x + Q.x * P.y)

    def convex(self):
        """
        Verifica se o polígono é convexo.

        Returns:
            bool: True se o polígono for convexo, False caso contrário.
        """
        if self.n < 3:
            return False  # Polígonos com menos de 3 lados não são convexos

        # Verifica se todos os ângulos internos têm a mesma orientação (horário ou anti-horário)
        orientation = self._D(self.vs[0], self.vs[1], self.vs[2])
        for i in range(1, self.n):
            if self._D(self.vs[i], self.vs[(i + 1) % self.n], self.vs[(i + 2) % self.n]) * orientation < 0:
                return False  # Ângulos com orientações diferentes, polígono não convexo
        return True

    def _distance(self, P: Point, Q: Point):
        """
        Calcula a distância euclidiana entre dois pontos.

        Args:
            P: Primeiro ponto.
            Q: Segundo ponto.

        Returns:
            float: A distância entre os pontos P e Q.
        """
        return hypot(P.x - Q.x, P.y - Q.y)

    def perimeter(self):
        """
        Calcula o perímetro do polígono.

        Returns:
            float: O perímetro do polígono.
        """
        p = 0.0
        for i in range(self.n):
            p += self._distance(self.vs[i], self.vs[i + 1])
        return p

    def area(self):
        """
        Calcula a área do polígono usando a fórmula de Shoelace.

        Returns:
            float: A área do polígono.
        """
        a = 0.0
        for i in range(self.n):
            a += self.vs[i].x * self.vs[i + 1].y
            a -= self.vs[i + 1].x * self.vs[i].y
        return 0.5 * fabs(a)

    def _angle(self, P: Point, A: Point, B: Point):
        """
        Calcula o ângulo entre os segmentos PA e PB.

        Args:
            P: Ponto comum aos segmentos.
            A: Ponto final do segmento PA.
            B: Ponto final do segmento PB.

        Returns:
            float: O ângulo entre os segmentos PA e PB em radianos.
        """
        ux = P.x - A.x
        uy = P.y - A.y
        vx = P.x - B.x
        vy = P.y - B.y
        num = ux * vx + uy * vy
        den = hypot(ux, uy) * hypot(vx, vy)
        return acos(num / den) if den else 0  # Trata caso de vetor degenerado (den == 0)

    def _equals(self, x: float, y: float):
        """
        Verifica se dois números de ponto flutuante são iguais dentro de uma tolerância.

        Args:
            x: Primeiro número.
            y: Segundo número.

        Returns:
            bool: True se os números forem considerados iguais, False caso contrário.
        """
        EPS = 1e-6
        return fabs(x - y) < EPS

    def contains(self, P: Point):
        """
        Verifica se um ponto está dentro do polígono (incluindo as bordas) usando a soma dos ângulos.

        Args:
            P: Ponto a ser verificado.

        Returns:
            bool: True se o ponto estiver dentro do polígono, False caso contrário.
        """
        if self.n < 3:
            return False  # Polígonos com menos de 3 lados não contêm pontos

        sum = 0.0
        for i in range(self.n):
            d = self._D(P, self.vs[i], self.vs[i + 1])
            a = self._angle(P, self.vs[i], self.vs[i + 1])
            sum += a if d > 0 else (-a if d < 0 else 0)  # Soma o ângulo ou seu negativo, dependendo da orientação

        return self._equals(fabs(sum), 2 * pi)  # Se a soma dos ângulos for 2*pi, o ponto está dentro

    def contains2(self, point: Point) -> bool:
        """
        Verifica se um ponto está dentro do polígono (incluindo as bordas) 
        usando o algoritmo Ray Casting.

        Args:
            point: O ponto a ser verificado.

        Returns:
            bool: True se o ponto estiver dentro do polígono, False caso contrário.
        """
        n = len(self.vs)
        inside = False

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
                inside = not inside

        return inside

    def _cross_product(self, p1: Point, p2: Point, p3: Point) -> float:
        """
        Calcula o produto vetorial entre os vetores p1p2 e p1p3.

        Args:
            p1: Ponto inicial dos vetores.
            p2: Ponto final do primeiro vetor.
            p3: Ponto final do segundo vetor.

        Returns:
            float: O produto vetorial. Um valor positivo indica que p3 está à esquerda de p1p2,
                   negativo indica que está à direita e zero indica que os pontos são colineares.
        """
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    def contains_cross_product(self, point: Point) -> bool:
        """
        Verifica se um ponto está dentro do polígono (incluindo as bordas) 
        usando o produto vetorial.

        Args:
            point: O ponto a ser verificado.

        Returns:
            bool: True se o ponto estiver dentro do polígono, False caso contrário.
        """
        for i in range(self.n):
            cross_product = self._cross_product(self.vs[i], self.vs[i + 1], point)
            if cross_product < 0:  # Ponto está à direita da aresta
                return False
            elif cross_product == 0:  # Ponto está sobre a aresta
                return True

        return True  # Ponto está dentro do polígono

    def _intersection(self, P: Point, Q: Point, A: Point, B: Point):
        """
        Calcula o ponto de intersecção entre os segmentos PQ e AB.

        Args:
            P: Ponto inicial do segmento PQ.
            Q: Ponto final do segmento PQ.
            A: Ponto inicial do segmento AB.
            B: Ponto final do segmento AB.

        Returns:
            Point: O ponto de intersecção entre os segmentos.
        """
        a = B.y - A.y
        b = A.x - B.x
        c = B.x * A.y - A.x * B.y
        u = fabs(a * P.x + b * P.y + c)
        v = fabs(a * Q.x + b * Q.y + c)
        return Point((P.x * v + Q.x * u) / (u + v), (P.y * v + Q.y * u) / (u + v))

    def cut_polygon(self, A: Point, B: Point):
        """
        Corta o polígono por uma linha definida pelos pontos A e B.
        Retorna um novo polígono formado pelos pontos que estão à esquerda da reta AB.

        Args:
            A: Ponto inicial da reta.
            B: Ponto final da reta.

        Returns:
            Polygon: O polígono resultante do corte.
        """
        points = []
        EPS = 1e-6

        for i in range(self.n):
            d1 = self._D(A, B, self.vs[i])
            d2 = self._D(A, B, self.vs[i + 1])

            if d1 > -EPS:  # Vértice está à esquerda da reta
                points.append(self.vs[i])

            if d1 * d2 < -EPS:  # A aresta cruza a reta
                points.append(self._intersection(self.vs[i], self.vs[i + 1], A, B))

        return Polygon(points)

    def circumradius(self):
        """
        Calcula o circunraio do polígono (apenas para polígonos regulares).

        Returns:
            float: O circunraio do polígono.
        """
        if self.n < 3:
            return 0  # Não definido para polígonos com menos de 3 lados
        s = self._distance(self.vs[0], self.vs[1])
        return (s / 2.0) * (1.0 / sin(pi / self.n))

    def apothem(self):
        """
        Calcula o apótema do polígono (apenas para polígonos regulares).

        Returns:
            float: O apótema do polígono.
        """
        if self.n < 3:
            return 0  # Não definido para polígonos com menos de 3 lados
        s = self._distance(self.vs[0], self.vs[1])
        return (s / 2.0) * (1.0 / tan(pi / self.n))

    def segment_angles(P, Q, R, S):
        """
        Calcula o ângulo entre os segmentos PQ e RS.

        Args:
            P: Ponto inicial do segmento PQ.
            Q: Ponto final do segmento PQ.
            R: Ponto inicial do segmento RS.
            S: Ponto final do segmento RS.

        Returns:
            float: O ângulo entre os segmentos PQ e RS em radianos, ou None se 
                   algum dos vetores for degenerado.
        """
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
```

**Observações:**

*   O código utiliza a classe auxiliar `Point` para representar pontos no plano cartesiano.
*   As funções que começam com `_` são consideradas internas à classe e não devem ser acessadas diretamente de fora da classe.
*   O parâmetro `EPS` (epsilon) é utilizado para lidar com imprecisões em cálculos de ponto flutuante.
