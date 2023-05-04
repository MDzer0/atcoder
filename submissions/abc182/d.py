N = int(input())
a = list(map(int, input().split()))
ans = 0
maxa = 0
rui = 0
tmp = 0
for i in a:
    rui += i
    maxa = max(maxa, rui)
    ans = max(ans, tmp + maxa)
    tmp += rui
print(ans)
