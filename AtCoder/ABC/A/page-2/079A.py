n = input()

if n[0] == n[1] == n[2] or n[1] == n[2] == n[3]:
    print("Yes")
else:
    print("No")


# n = list(map(int, input()))
# count = 0
# for i in range(len(n)-1):
#     if n[i] == n[i+1]:
#         count += 1
#         if count == 2:
#             break
#     else:
#         count = 0
# print("Yes") if count == 2 else print("No")
