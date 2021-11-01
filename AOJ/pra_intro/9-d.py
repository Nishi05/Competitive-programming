c = str(input())
n = int(input())

for i in range(n):
    opt = list(map(str, input().split()))
    a = int(opt[1])
    b = int(opt[2])
    if opt[0] == "print":
        print(c[a:b+1])
    elif opt[0] == "replace":
        x = opt[3]
        c = c[:a] + x + c[b+1:]
    elif opt[0] == "reverse":
        mid = c[a:b+1]
        c = c[:a] + mid[::-1] + c[b+1:]
