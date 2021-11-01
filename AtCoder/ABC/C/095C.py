a, b, c, x, y = map(int, input().split())
pizza = [a, b, c]
nums = [x, y]

if a + b < c*2:
    print((a*x)+(b*y))
else:
    if a > c*2 and b > c*2:
        print(2*c*max(x, y))
    else:
        cnum = min(x, y)
        cfee = 2*c*cnum
        if ()
        # if x > y:
        #     abfee = a*(x-y)
        # else:
        #     abfee = b*(y-x)
        print(abfee + cfee)
