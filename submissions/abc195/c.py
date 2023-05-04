N = int(input())
cnt = 1
ans = 0
tmp = '999'

while N > int(tmp * cnt):
    ans += N - int(tmp * cnt)
    cnt += 1
print(ans)
