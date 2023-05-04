N = int(input())
A = list(map(int, input().split()))
cnt = 1
ans = 1
for i in A:
    if i == 1:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

print(max(ans, cnt))
