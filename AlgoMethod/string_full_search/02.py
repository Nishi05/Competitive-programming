s = str(input())

for i in range(len(s)):
    if s[i] != s[len(s)-i - 1]:
        print("No")
        break
else:
    print("Yes")
