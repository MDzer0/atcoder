N=int(input())
if N%2==1:
    print("error")
    exit()
l=list(map(int,input().split()))
ans=(l[-1]-l[0])
L=l[1:N-1]
#print(L)
for i in range(N-2):
    if i%2==0:
        ans+=L[i]
    else:
        ans-=L[i]
print(ans)
