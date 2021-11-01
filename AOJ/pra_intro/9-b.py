while True:
    char = str(input())
    if char == "-":
        break
    n = int(input())
    for i in range(n):
        C = int(input())
        tmp = char[C:] + char[0:C]
        char = tmp
    print(char)
