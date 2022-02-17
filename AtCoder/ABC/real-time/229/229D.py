s = str(input())
k = int(input())
cnt = 0
life = k
n = 0
for i in range(len(s)):
    m = 0
    while life != 0 and s[i+m] != '.':
        if s[i+m] == 'X':
            cnt += 1
        else:
            cnt += 1
            life -= 1
        m += 1
    n = max(n, cnt)
    cnt = 0
print(max(n, cnt))
