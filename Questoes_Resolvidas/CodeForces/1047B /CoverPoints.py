n = int(input())
soma = 0

for _ in range(n):
    x, y = map(int, input().split())
    soma = max(soma, x + y)

print(soma)