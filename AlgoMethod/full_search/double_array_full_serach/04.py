s = str(input())
lst = []
for i in s:
    if i not in lst:
        lst.append(i)
print(len(lst))
