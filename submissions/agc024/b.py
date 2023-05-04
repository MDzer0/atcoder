n = int(input())
l = [0]*(n+1)
for i in range(n):
    x = int(input())
    l[x] = l[x-1]+1

print(n-max(l))
