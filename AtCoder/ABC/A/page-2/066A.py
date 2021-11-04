# listでとってきてsortとして小さい順から二つ足していく
list = list(map(int, input().split()))
list.sort()
print(list[0]+list[1])
