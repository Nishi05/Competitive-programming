n = int(input())
s = str(input())

s_lst = [0]
x = 0
s_lst.append(x)
for i in s:
    if i == "I":
        x += 1
        s_lst.append(x)
    else:
        x -= 1
        s_lst.append(x)

print(max(s_lst))
