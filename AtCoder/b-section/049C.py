S = str(input())

S = S[::-1]
T = ["dream", "dreamer", "erase", "eraser"]
T = [RT[::-1] for RT in T]

i = 0
can = True
while i < len(S):
    can2 = False
    for j in T:
        if S[i:len(j)+i] == j:
            can2 = True
            i += len(j)
            break

    if can2 == False:
        can = False
        break
if can:
    print("YES")
else:
    print("NO")
