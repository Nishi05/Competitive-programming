s = str(input())

lst = [False]*26

for i in s:
    k = ord(i) - 97
    lst[k] = True

for idx, j in enumerate(lst):
    if j == False:
        print(chr(idx + 97))
        break
else:
    print("None")
