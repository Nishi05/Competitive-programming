n = int(input())
list = []
for _ in range(n):
    s = str(input())[1:]

    list.append(''.join(s))
print(len(dict.fromkeys(list)))
