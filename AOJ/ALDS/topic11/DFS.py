
def dfs(i):
    global t
    for j in G[i]:
        if d[j] == -1:
            t += 1
            d[j] = t
            dfs(j)
    t += 1
    f[i] = t
    return


n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[1] > 0:
        G[lst[0]] = lst[2:]
d = [-1]*(n+1)
f = [-1]*(n+1)
t = 0

for i in range(1, n+1):
    if d[i] == -1:
        t += 1
        d[i] = t
        dfs(i)
for i in range(1, n+1):
    print(i, d[i], f[i])
