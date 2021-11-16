# 最大の利益
n = int(input())

lst = [int(input()) for _ in range(n)]

minv = lst[0]
maxv = lst[1] - lst[0]
for i in range(1, n):
    maxv = max(maxv, lst[i] - minv)
    minv = min(minv, lst[i])
print(maxv)
