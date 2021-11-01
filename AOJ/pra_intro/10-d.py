n = int(input())

x = list(map(float, input().split()))
y = list(map(float, input().split()))

p1 = 0
p2 = 0
p3 = 0
px = 0

for i in range(n):
    p1 += abs(x[i] - y[i])
    p2 += (abs(x[i] - y[i]))**2
    p3 += (abs(x[i] - y[i]))**3
    px = max(px, abs(x[i] - y[i]))

print(p1)
print(p2**(1/2))
print(p3**(1/3))
print(px)
