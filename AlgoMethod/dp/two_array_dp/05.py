n = int(input())

lst = [input() for _ in range(n)]
n_lst = [[0]*n for _ in range(n)]
n_lst[0][0] = 1
for i in range(n):
    for j in range(n):
        # #の時は弾く
        if lst[i][j] == '#':
            continue
        if i - 1 >= 0:
            n_lst[i][j] += n_lst[i-1][j]
        if j - 1 >= 0:
            n_lst[i][j] += n_lst[i][j-1]
print(n_lst[n-1][n-1])
