t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    area_maxima = 0

    k, *a = map(int, input().split())
    area_maxima = max(area_maxima, (a[-1] - a[0]) * h )
    k, *a = map(int, input().split())
    area_maxima = max(area_maxima, (a[-1] - a[0]) * h )
    k, *a = map(int, input().split())
    area_maxima = max(area_maxima, (a[-1] - a[0]) * w )
    k, *a = map(int, input().split())
    area_maxima = max(area_maxima, (a[-1] - a[0]) * w )

    print(area_maxima)
