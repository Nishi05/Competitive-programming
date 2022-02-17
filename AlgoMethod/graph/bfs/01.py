N, M = map(int, input().split())


G = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

dist = [-1] * N
nodes = [[] for _ in range(N)]
dist[0] = 0
nodes[0] = [0]

for k in range(1, N):
    for v in nodes[k-1]:
        print('v', nodes[k-1])
        for next_v in G[v]:
            print('next_v', G[v])
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            nodes[k].append(next_v)
