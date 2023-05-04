from collections import deque

N = int(input())
A = list(map(int, input().split()))
ans = []
d = deque()

for i in range(N):
    if i >= 1:
        d.append((i, A[i - 1]))
        while d:
            tmp = d[-1][1]
            if tmp > A[i]:
                break
            else:
                d.pop()
    if not d:
        ans.append(-1)
    else:
        ans.append(d[-1][0])
print(*ans)
