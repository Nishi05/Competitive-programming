n = int(input())
for i in range(n+1):
    if i % 3 == 0 or ('3' in str(i)):
        print(i, end=' ')
