lst = [list(map(int, input().split())) if i == 0 else [0]*4 for i in range(4)]

for i in range(4):
    for j in range(4):
        if i - 1 >= 0:
            lst[i][j] += lst[i-1][j]
            if j - 1 >= 0:
                lst[i][j] += lst[i-1][j-1]
            if j + 1 < 4:
                lst[i][j] += lst[i-1][j+1]
print(lst[3][3])
