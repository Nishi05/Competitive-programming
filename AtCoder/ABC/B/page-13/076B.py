n = int(input())
k = int(input())
num = 1
for _ in range(n):
    if num * 2 > num + k:
        num += k
    else:
        num *= 2

print(num)
