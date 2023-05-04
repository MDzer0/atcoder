from collections import defaultdict
N = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)

for i in a:
    while True:
        v, m = divmod(i, 2)
        if m != 0:
            d[v] += 1
            break
        i = v

print(len(d))
