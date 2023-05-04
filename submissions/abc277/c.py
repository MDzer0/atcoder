from collections import defaultdict, deque

N = int(input())
hashigo = defaultdict(list)

for i in range(N):
    A, B = map(int, input().split())
    hashigo[A].append(B)
    hashigo[B].append(A)

q = deque()
q.append(1)
ans = 1
tmp = {1}
while q:
    v = q.popleft()
    for i in hashigo[v]:
        if i not in tmp:
            q.append(i)
            tmp.add(i)
            ans = max(ans, i)

print(ans)
