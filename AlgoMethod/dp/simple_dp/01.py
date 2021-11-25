n, x, y = map(int, input().split())
lst = [0]*n
lst[0] = x
lst[1] = y
for i in range(2, n):
    lst[i] = (lst[i-2] + lst[i-1]) % 100
print(lst[-1])
