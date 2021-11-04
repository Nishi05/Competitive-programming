a, b = map(int, input().split())
c = a + b
print('Possible') if c % 3 == 0 or a % 3 == 0 or b % 3 == 0 else print('Impossible')
