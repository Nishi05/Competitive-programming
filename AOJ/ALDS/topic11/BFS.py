n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(1, n+1):
    lst = list(map(int, input().split()))
    if lst[1] > 0:
        G[lst[0]] = lst[2:]

q = []
q.append(1)
checked = [False]*(n+1)
checked[1] = True
d = [-1] * (n+1)
d[1] = 0

while q:
    current = q.pop(0)
    for i in G[current]:
        if not checked[i]:
            q.append(i)
            checked[i] = True
            d[i] = d[current] + 1


for i in range(1, n+1):
    print(i, d[i])
