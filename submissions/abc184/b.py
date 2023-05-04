N, X = map(int, input().split())
S = input()
ans = X
for i in S:
    if 'x' == i:
        if ans > 0:
            ans -= 1
    else:
        ans += 1

print(ans)
