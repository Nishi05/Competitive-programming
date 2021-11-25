n = int(input())
lst = [list(map(int, input().split())) if i == 0 else [0]*n for i in range(n)]

for i in range(1, n):
    for j in range(n):
        lst[i][j] += lst[i-1][j]
        if j - 1 >= 0:
            lst[i][j] += lst[i-1][j-1]
        if j + 1 < n:
            lst[i][j] += lst[i-1][j+1]
        lst[i][j] = lst[i][j] % 100
print(lst[n-1][n-1])
