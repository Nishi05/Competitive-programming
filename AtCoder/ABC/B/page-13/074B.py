n = int(input())
k = int(input())

lst = list(map(int, input().split()))
dis = 0
for i in range(n):
    if abs(lst[i] - 0) > abs(lst[i] - k):
        dis += abs(lst[i] - k)*2
    else:
        dis += abs(lst[i] - 0)*2
print(dis)
