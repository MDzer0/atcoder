from collections import defaultdict

S = input()
d = defaultdict(int)
for i in S:
    d[i] += 1

comp = d[S[0]]
for v, m in d.items():
    if comp != m:
        print('No')
        exit()
print('Yes')
