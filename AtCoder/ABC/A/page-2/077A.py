a = str(input())
b = str(input())

if a == b[::-1] and b == a[::-1]:
    print("YES")
else:
    print("NO")
