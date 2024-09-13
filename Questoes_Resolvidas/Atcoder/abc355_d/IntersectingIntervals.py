N = int(input())
v = [tuple(map(int,input().split())) for _ in range(0,N)]
balela = []

for i in range(0,N):
    balela.append((v[i][0],0))
    balela.append((v[i][1],1))

balela.sort()

inter = 0
gremio = 0

for point, event_type in balela:
    if event_type == 0:
        inter += gremio
        gremio += 1
    else: 
        gremio -= 1 

print(inter)