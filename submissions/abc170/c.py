X, N = map(int, input().split())
p = list(map(int, input().split()))
ans = X
for i in range(101):
    ans = X - i
    if ans in p:
        ans = X + i
        if ans in p:
            continue
        else:
            break
    else:
        break

print(ans)
