n, q = map(int, input().split())
queue = [list(input().split()) for _ in range(n)]
time = 0
while queue:
    s, t = queue.pop(0)
    t = int(t)
    if q >= t:
        time += t
        print(s, time)
    else:
        time += q
        queue.append([s, t-q])
