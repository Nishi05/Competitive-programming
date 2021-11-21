n, x = map(int, input().split())
lst = list(map(int, input().split()))
n_lst = [False]*n
n_lst[x-1] = True
m = lst[x-1]
while 1:
    if n_lst[m-1] == False:
        n_lst[m-1] = True
        m = lst[m-1]
    else:
        break
print(n_lst.count(True))


# n, x = map(int, input().split())
# lst = list(map(int, input().split()))


# s = str(x)
# m = lst[x-1]
# m = str(m)
# cnt = 1
# for i in range(n):
#     if m not in s:
#         s += m
#         m = lst[int(m)-1]
#         m = str(m)
#         cnt += 1
#     else:
#         break
# # print(len(n_lst))
# print(cnt)
