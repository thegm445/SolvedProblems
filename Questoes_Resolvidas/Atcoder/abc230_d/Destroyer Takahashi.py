def min_punches(D, walls):
    walls.sort(key=lambda x: x[1])
    punches = 0
    rightmost_destroyed = 0

    for L, R in walls:
        if L <= rightmost_destroyed:
            continue
        punches += 1
        rightmost_destroyed = R + D - 1

    return punches



N, D = map(int, input().split())
walls = [tuple(map(int, input().split())) for _ in range(N)]
result = min_punches(D, walls)
print(result)
