import collections
n = int(input())
q_lst = collections.deque()
for _ in range(n):
    s = input()
    if s == 'deleteFirst':
        q_lst.popleft()
    elif s == 'deleteLast':
        q_lst.pop()
    else:
        com, num = s.split()
        if com == 'insert':
            q_lst.appendleft(num)
        elif com == 'delete':
            try:
                q_lst.remove(num)
            except:
                pass

print(' '.join(q_lst))
