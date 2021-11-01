n = int(input())
card = list(map(int, input().split()))
Alice = 0
Bob = 0
card.sort(reverse=True)
for i in range(n):
    if (i + 1) % 2 != 0:
        Alice += card[i]
    else:
        Bob += card[i]
print(Alice - Bob)
