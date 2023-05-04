from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
    S = input()
    d[S] += 1
    if d[S] == 1:
        print(i + 1)
