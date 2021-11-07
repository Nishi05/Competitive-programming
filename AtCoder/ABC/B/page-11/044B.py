s = list(map(str, input()))
s.sort()
flg = True
count = 0
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        count += 1
    else:
        if count % 2 == 0:
            flg = False
            break
        count = 0
if len(s) == 1:
    flg = False
print("Yes") if flg else print("No")
