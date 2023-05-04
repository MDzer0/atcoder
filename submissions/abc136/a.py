A, B, C = map(int, input().split())
tmp = A - B
ans = C -tmp
if ans < 0 :
    ans = 0
print(ans)
