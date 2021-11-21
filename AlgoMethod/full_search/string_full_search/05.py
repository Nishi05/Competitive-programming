s = str(input())
t = str(input())
n = len(t)
for i in range(len(s)):
    if s[i] == t[0]:
        cnt = 1
        for j in range(1, len(t)):
            if i+j <= len(s) - 1:
                if s[i+j] == t[j]:
                    cnt += 1
        if n == cnt:
            print("Yes")
            break
else:
    print("No")
