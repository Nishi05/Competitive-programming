s = str(input())
num = 0
for n in s:
    num += int(n)
print('Yes') if int(s) % num == 0 else print('No')
