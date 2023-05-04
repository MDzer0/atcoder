from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

da = defaultdict(int)
db = defaultdict(int)

for i in A:
    da[i] += 1

for i in C:
    db[B[i - 1]] += 1

ans = 0
for i, j in db.items():
    ans += da[i] * j
print(ans)
