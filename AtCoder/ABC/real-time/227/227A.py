n, k, a = map(int, input().split())

m = a
for _ in range(k-1):
    if m == n:
        m = 0
    m += 1
print(m)
