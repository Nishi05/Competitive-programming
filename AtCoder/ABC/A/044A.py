# for文で宿泊数を表現する
n = int(input())
k = int(input())
x = int(input())
y = int(input())

sum = 0
for i in range(1, n+1):
    if i <= k:
        sum += x
    else:
        sum += y

print(sum)
