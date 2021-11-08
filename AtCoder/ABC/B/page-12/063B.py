s = str(input())

s_lst = []

for i in s:
    if i not in s_lst:
        s_lst.append(i)
    else:
        print("no")
        break
else:
    print("yes")
