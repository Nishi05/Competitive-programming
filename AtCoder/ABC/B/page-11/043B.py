s = str(input())
ans = ''

for i in s:
    if i == 'B':
        ans = ans[:-1]
    else:
        ans += i

print(ans)


# list = []
# for i in s:
#     if i == "0" or i == "1":
#         list.append(i)
#     else:
#         if len(list) != 0:
#             list.pop(-1)

# print(''.join(list))
