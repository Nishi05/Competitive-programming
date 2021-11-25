n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
n_lst = [[0]*n for _ in range(n)]
n_lst[0][0] = lst[0][0]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        a = 0
        b = 0
        if i - 1 >= 0:
            a = lst[i][j] + n_lst[i-1][j]
        if j - 1 >= 0:
            b = lst[i][j] + n_lst[i][j-1]
        n_lst[i][j] = max(a, b)
print(n_lst[n-1][n-1])
