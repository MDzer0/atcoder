from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
total = 0
for i in a:
    d[i] += 1
    total += i
Q = int(input())

for i in range(Q):
    b, c = map(int, input().split())
    cnt = d[b]
    total -= cnt * b
    d[b] = 0
    d[c] += cnt
    total += c * cnt
    print(total)
