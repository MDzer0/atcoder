N = int(input())
A = list(map(int, input().split()))

piza = [0] * 361
kirime = 0
piza[0] = 1
for i in A:
    kirime += i
    kirime %= 360
    piza[kirime] = 1

ans = 0
cnt = 0
for i in piza:
    cnt += 1
    ans = max(ans, cnt)
    if i == 1:
        cnt = 0

print(ans)
