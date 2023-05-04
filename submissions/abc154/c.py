from collections import defaultdict
N = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
for i in a:
    d[i] += 1

for i in d.values():
    if i != 1:
        print('NO')
        exit()

print('YES')
