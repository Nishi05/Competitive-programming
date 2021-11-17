n = int(input())
lst = list(map(int, input().split()))

print(lst.index(max(lst)))

# 線形探索
# index = 0
# for i in range(N):
#     if lst[i] > lst[index]:
#         index = i
