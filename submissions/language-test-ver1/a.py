from collections import defaultdict

N = int(input())
c = input()
d = defaultdict(int)
for i in range(N):
    d[int(c[i])] += 1

ans1, ans2 = 0, 10 ** 10
for i in range(4):
    ans1 = max(ans1, d[i + 1])
    ans2 = min(ans2, d[i + 1])
print(ans1, ans2)
