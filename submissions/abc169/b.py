INF = 10 ** 18
N = int(input())
a = list(map(int, input().split()))
ans = 1
if a.count(0) > 0:
    print(0)
    exit()
for i in a:
    ans *= i
    if ans > INF:
        print(-1)
        exit()

print(ans)
