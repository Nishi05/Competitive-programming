n = int(input())

lst = [[0]*n for _ in range(n)]

lst[0][0] = 1

for i in range(n):
    for j in range(n):
        if i - 1 >= 0:
            lst[i][j] += lst[i-1][j]
        if j - 1 >= 0:
            lst[i][j] += lst[i][j-1]
print(lst[n-1][n-1])
