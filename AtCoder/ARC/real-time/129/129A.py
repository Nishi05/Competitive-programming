import math
N, L, R = map(int, input().split())

cnt = 0
# i = L
# while i <= math.sqrt(R):
#     num = i ^ N
#     if num < N:
#         cnt += 1
#     i += 1
for i in range(L, R+1):
    num = i ^ N
    if num < N:
        cnt += 1
print(cnt)
