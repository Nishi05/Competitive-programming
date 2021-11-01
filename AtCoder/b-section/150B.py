n = int(input())
s = str(input())
count = 0
for i in range(n-2):
    if s[i]+s[i+1]+s[i+2] == "ABC":
        count += 1
print(count)
