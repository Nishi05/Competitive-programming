n = int(input())
cnt = 0

for i in range(n):
    s = str(input())
    r = s[::-1]
    if s == r:
        cnt += 1
print(cnt)
