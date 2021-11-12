n = int(input())
lst = [2, 1]
if n == 1:
    print(1)
    exit()
for i in range(2, n+1):
    lst.append(lst[i-1]+lst[i-2])
print(lst[-1])
