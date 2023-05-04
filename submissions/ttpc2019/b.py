import re

pattern = '.*okyo.*ech.*'
N = int(input())
for i in range(N):
    s = input()
    ans = re.match(pattern, s)
    if ans != None:
        print('Yes')
    else:
        print('No')
