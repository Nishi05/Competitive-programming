INF = 1000000
n, m = map(int, input().split())
lst = list(map(int, input().split()))

t = [INF]*n
t[0] = 0

for i in range(1, n):
    for j in range(1, m+1):
        if i - j >= 0:
            t[i] = min(t[i], t[i-j]+lst[i]*j)
print(t[-1])
