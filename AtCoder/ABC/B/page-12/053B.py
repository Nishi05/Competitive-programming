s = str(input())
a, b = 0, 0
for i in range(len(s)):
    if s[i] == "A":
        a = i
        break

for i in range(len(s)-1, 0, - 1):
    if s[i] == "Z":
        b = i
        break
print(b-a+1)
