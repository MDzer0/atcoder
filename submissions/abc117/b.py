N = int(input())
llst = list(map(int, input().split()))
llst.sort(reverse=True)
p = 0
for i in range(N - 1):
    p += llst[i + 1]
if llst[0] < p:
    print('Yes')
else:
    print('No')
