from collections import deque
N, X = map(int, input().split())
A = list(input())
A[X - 1] = '@'
d = deque()
d.append(X - 1)
d.append(X + 1)
while d:
    tmp = d.pop()
    if tmp != 0 and tmp != N + 1:
        if A[tmp - 1] == '.':
            A[tmp - 1] = '@'
            d.append(tmp - 1)
            d.append(tmp + 1)

for i in A:
    print(i, end='')
