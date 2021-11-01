s = list(map(str, input()))
p = input()

count = 0
for c in p:
    if(c in s):
        count += 1

if(count == len(p)):
    print("Yes")
else:
    print("No")
