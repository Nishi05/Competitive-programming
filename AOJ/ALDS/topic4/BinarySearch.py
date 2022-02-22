n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

def binarySearch(key):
    left = 0
    right = n
    while left < right:
        mid = int((left + right) / 2)
        if S[mid] == key:
            return True
        elif key < S[mid]:
            right = mid
        else:
            left = mid + 1
    return False

count = 0
for j in T:
    if binarySearch(j):
        count += 1
print(count)
