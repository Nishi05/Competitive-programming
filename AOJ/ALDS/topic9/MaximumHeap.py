n = int(input())
A = [0] + [int(i) for i in input().split()]


def maxHeapify(i):
    left = 2 * i
    right = 2 * i + 1

    if left <= n and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right <= n and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(largest)


for i in range(int(n/2), 0, -1):
    maxHeapify(i)

print('', *A[1:])
