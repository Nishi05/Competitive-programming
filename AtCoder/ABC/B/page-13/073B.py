n = int(input())

cnt = 0
for _ in range(n):
    l, r = map(int, input().split())
    cnt += (r - l) + 1
print(cnt)
