S = str(input())
count = 0
list = [0]
for i in S:
    if i in "ACGT":
        count += 1
    else:
        list.append(count)
        count = 0
list.append(count)
print(max(list))
