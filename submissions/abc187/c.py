from collections import defaultdict
N = int(input())
s = [input() for _ in range(N)]

d = defaultdict(int)
for i in range(N):
    d[s[i]] += 1

for k in d.keys():
    if '!' + k in d:
        print(k)
        exit()

print('satisfiable')
