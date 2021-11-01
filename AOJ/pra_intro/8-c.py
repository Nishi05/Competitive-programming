list = [0]*26
while True:
    try:
        str = input().lower()
        for i in str:
            if "a" <= i and i <= "z":
                num = ord(i) - ord("a")
                list[num] += 1
    except EOFError:
        break

for i in range(26):
    print("{} : {}".format(chr(i + 97), list[i]))
