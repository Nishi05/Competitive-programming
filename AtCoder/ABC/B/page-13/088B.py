n = int(input())

lst = list(map(int, input().split()))

lst.sort(reverse=True)

a = 0
b = 0
for i in range(1, n+1):
    if i % 2 == 0:
        b += lst[i-1]
    else:
        a += lst[i-1]
print(a-b)
