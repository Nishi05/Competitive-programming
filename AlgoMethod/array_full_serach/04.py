n, v = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    if lst[i] == v:
        print(i)
        break
else:
    print(-1)
