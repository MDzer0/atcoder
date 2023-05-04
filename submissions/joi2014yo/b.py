N,M=map(int,input().split())
A=[int(input()) for i in range(N)]
B=[int(input()) for i in range(M)]
X=[0 for i in range(N)]
for j in range(M):
    for i in range(N):
        if A[i]<=B[j]:
            X[i]+=1
            break
Y=[(X[i],i+1) for i in range(N)]
print(max(Y)[1])
