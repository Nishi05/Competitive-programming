# import sys

# INF = 1 << 30
# A = [0]*2000001
# n = 0


# def maxHeapify(i):
#     left = 2 * i
#     right = 2 * i + 1

#     if left <= n and A[left] > A[i]:
#         largest = left
#     else:
#         largest = i
#     if right <= n and A[right] > A[largest]:
#         largest = right

#     if largest != i:
#         A[i], A[largest] = A[largest], A[i]
#         maxHeapify(largest)


# def extract():
#     global n
#     if n < 1:
#         return INF
#     maxv = A[1]
#     A[1] = A[n]
#     n -= 1
#     maxHeapify(1)
#     return maxv


# def increaseKey(i, key):
#     if key < A[i]:
#         return
#     A[i] = key
#     while i > 1 and A[int(i/2)] < A[i]:
#         A[i], A[int(i/2)] = A[int(i/2)], A[i]
#         i = int(i/2)


# def insert(key):
#     global n
#     n += 1
#     A[n] = -INF
#     increaseKey(n, key)


# S = []
# while 1:
#     line = sys.stdin.readline().split()
#     if line[0] == 'end':
#         print(*S, sep='\n')
#         break
#     elif line[0] == 'insert':
#         insert(int(line[1]))
#     else:
#         S.append(extract())


import heapq
import sys
a = [0]
heapq.heapify(a)


for s in sys.stdin:
    if s[1] == 'x':
        print(heapq.heappop(a) * (-1))

    elif s[0] == 'i':
        num = int(s[7:]) * (-1)
        heapq.heappush(a, num)
