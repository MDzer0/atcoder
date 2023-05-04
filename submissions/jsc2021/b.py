from collections import defaultdict

def create_dict(V):
    for i in V:
        d[i] += 1

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = defaultdict(int)
create_dict(A)
create_dict(B)

ans = []
for v, m in d.items():
    if m == 1:
        ans.append(v)
ans.sort()

print(*ans)
