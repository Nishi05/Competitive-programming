s, t, x = map(int, input().split())
lst = [False]*24

if s < t:
    for i in range(s, t+1):
        lst[i] = True
else:
    for i in range(s, 24):
        lst[i] = True
    for i in range(0, t):
        lst[i] = True

print("Yes") if lst[x] == True else print("No")
