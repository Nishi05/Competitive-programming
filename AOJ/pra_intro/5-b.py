while True:
    H, W = map(int, input().split())
    if W == 0 and H == 0:
        break
    for i in range(H):
        for l in range(W):
            if l % 2 == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
