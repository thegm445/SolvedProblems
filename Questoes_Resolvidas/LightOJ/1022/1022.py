from math import acos

pi = 2 * acos(0.0)

n = int(input())

for i in range(1,n+1):
    r = float(input())
    square_side = 2*r

    circle_area = pi*r**2
    square_side *= square_side

    print(f"Case {i}: {(square_side-circle_area):.2f}")
