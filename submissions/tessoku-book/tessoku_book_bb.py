from collections import defaultdict

Q = int(input())
d = defaultdict(int)
for i in range(Q):
    query = list(input().split())
    if int(query[0]) == 1:
        d[query[1]] = int(query[2])
    else:
        print(d[query[1]])
