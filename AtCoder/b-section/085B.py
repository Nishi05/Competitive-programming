n = int(input())
count = 1
list = [int(input()) for i in range(n)]

list.sort(reverse=True)

for i in range(n-1):
    if(list[i] == list[i+1]):
        continue
    else:
        count += 1

print(count)
