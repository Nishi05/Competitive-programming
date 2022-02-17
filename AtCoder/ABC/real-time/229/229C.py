n, w = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(reverse=True)
amount = 0
for i in range(n):
    if w >= lst[i][1]:
        amount += lst[i][0]*lst[i][1]
        w -= lst[i][1]
    else:
        amount += lst[i][0]*w
        break
print(amount)
