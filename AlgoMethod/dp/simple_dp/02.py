n = int(input())
lst = list(map(int, input().split()))
t = [0]*n
t[1] = lst[1]

for i in range(2, n):
    t[i] = min(t[i-1]+lst[i], lst[i]*2 + t[i-2])
print(t[-1])
