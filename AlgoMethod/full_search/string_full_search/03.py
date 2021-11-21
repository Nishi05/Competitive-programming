s = str(input())
cnt = 0
for i in range(0, len(s)-1):
    if s[i] == s[i+1]:
        cnt += 1
else:
    print(cnt)
