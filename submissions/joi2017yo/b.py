N,M=map(int,input().split())
ab=sorted([tuple(map(int,input().split())) for _ in range(M)],reverse=True)
ans=0
for i in range(M-1):
    ans+=max(0,N-ab[i][0])
print(ans)
