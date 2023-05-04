N = int(input())
S = [input() for _ in range(N)]
slist = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
ans = []
for i in S:
    print(slist[(slist.index(i) + 1) % 7])
