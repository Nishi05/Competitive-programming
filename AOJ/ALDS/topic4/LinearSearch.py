n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
S.append(0)
def linearSearch(key,n):
    i = 0
    S[n] = key
    while S[i] != key:
        i += 1
    if i >= n:
        return False
    return True
count = 0
for j in T:
    if linearSearch(j,n):
        count += 1
print(count)