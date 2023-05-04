n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    ans=ans*2+a[i]
print(ans)
