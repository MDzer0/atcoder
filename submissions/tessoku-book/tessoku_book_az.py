from collections import deque
Q = int(input())
d = deque()

for i in range(Q):
    query = list(input().split())
    if int(query[0]) == 1:
        d.append(query[1])
    elif int(query[0]) == 2:
        print(d[0])
    else:
        d.popleft()
