N = int(input())
ans = 0
while True:
    if N >= 7:
        ans += 100
        N -= 10
    else:
        break
if N > 0:
    ans += N * 15
print(ans)
