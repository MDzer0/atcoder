import sys
n, d = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n-1):
  if l[i+1]-l[i] <= d:
    print(l[i+1])
    sys.exit()
print(-1)
