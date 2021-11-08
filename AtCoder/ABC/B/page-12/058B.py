o = str(input())
e = str(input())
s = ''
for i in range(len(e)):
    s += o[i] + e[i]
if len(o) - len(e) == 1:
    s += o[-1]
print(s)
