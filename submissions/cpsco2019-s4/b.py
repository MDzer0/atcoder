import itertools

N,D = map(int,input().split())
S = [input() for _ in range(D)]
ans = 0

for p in itertools.product(range(2),repeat=D):
    if sum(p)!=2:
        continue
    else:
        cnt = set()
        for i in range(D):
            if p[i]==1:
                for j in range(N):
                    if S[i][j]=='o':
                        cnt.add(j)
        ans=max(ans,len(cnt))
print(ans)
