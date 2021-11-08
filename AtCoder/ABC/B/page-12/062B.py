n, m = map(int, input().split())

print("#"*(m+2))
for _ in range(n):
    print("#" + str(input()) + "#")
print("#"*(m+2))
