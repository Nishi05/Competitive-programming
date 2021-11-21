n = int(input())
s = str(input())
cnt = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        if s[i] == s[j]:
            cnt += 1
print(cnt)
