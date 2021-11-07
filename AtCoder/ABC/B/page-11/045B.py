a = list(input())
b = list(input())
c = list(input())

s = a.pop(0)
while 1:
    if s == "a":
        if len(a) != 0:
            s = a.pop(0)
        else:
            print("A")
            break
    elif s == "b":
        if len(b) != 0:
            s = b.pop(0)
        else:
            print("B")
            break
    elif s == "c":
        if len(c) != 0:
            s = c.pop(0)
        else:
            print("C")
            break
