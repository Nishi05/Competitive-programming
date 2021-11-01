row, col = map(int, input().split())
matrix = [[] for i in range(row)]
for i in range(row):
    matrix[i] = list(map(int, input().split()))


vec = [0]*col

for i in range(col):
    vec[i] = int(input())

for i in range(row):
    ip = 0
    for j in range(col):
        ip += matrix[i][j] * vec[j]
    print(ip)
