w, a, b = map(int, input().split())

aw = a + w
bw = b + w

if a > b:
    c = a - bw
else:
    c = b - aw

print(c) if c >= 0 else print(0)
