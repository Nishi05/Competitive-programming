s = str(input())
for i in range(len(s)-1, 0, -1):
    if i % 2 == 1:
        continue
    m = s[:i]
    k = int(i/2)
    if m[:k] == m[k:]:
        print(i)
        break
else:
    print(2)
