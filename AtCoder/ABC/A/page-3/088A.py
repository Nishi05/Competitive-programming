n = int(input())
a = int(input())

if a > n or a > n % 500 or n % 500 == 0:
    print("Yes")
else:
    print("No")
