n = int(input())
flg = True
for i in range(n-1):
    a, b = map(int, input().split())
    if i == 0:
        tmp_a = a
        tmp_b = b
    elif i == 1:
        if tmp_a == a or tmp_a == b:
            key_val = tmp_a
        elif tmp_b == a or tmp_b == b:
            key_val = tmp_b
        else:
            flg = False
            break
    else:
        if key_val != a and key_val != b:
            flg = False
            break
        else:
            continue
if flg:
    print("Yes")
else:
    print("No")
