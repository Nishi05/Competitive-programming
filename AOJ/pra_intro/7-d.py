n, m, l = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]

C = [[0]*l for _ in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += a[i][k] * b[k][j]

for line in C:
    print(*line)
