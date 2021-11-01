n, a, b = map(int, input().split())
total = 0
for c in range(1, n+1):
    sum = 0
    for i in str(c):
        print(i)
        sum += int(i)
    if a <= sum and sum <= b:
        total += c
print(total)
