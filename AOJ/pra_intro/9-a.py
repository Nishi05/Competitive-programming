W = str(input())
count = 0
while True:
    T = list(map(str, input().split()))

    if(T[0] == "END_OF_TEXT"):
        break
    for word in T:
        if(W == word.lower()):
            count += 1

print(count)
