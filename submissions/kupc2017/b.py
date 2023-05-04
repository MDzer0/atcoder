N, S, T = map(int, input().split())
tmp = T
ans = 0
while(tmp >= S):
    if tmp == S:
        print(ans)
        break
    ans += 1
    tmp //= 2
else:
    print(-1)
