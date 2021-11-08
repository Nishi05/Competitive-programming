n, m = map(int, input().split())

road = [0]*n

for i in range(m):
    a, b = map(int, input().split())
    road[a-1] += 1
    road[b-1] += 1

for j in range(n):
    print(road[j])
