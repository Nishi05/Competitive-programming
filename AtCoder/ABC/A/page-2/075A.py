list = list(map(int, input().split()))

list.sort()

if list[0] == list[1]:
    print(list[2])
else:
    print(list[0])
