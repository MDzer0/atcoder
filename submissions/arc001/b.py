A, B = map(int, input().split())
tmp = abs(A - B)
ans = 0
ans += tmp // 10
tmp = tmp % 10
if tmp >= 8:
    ans += abs(10 - tmp) + 1
elif tmp >= 3:
    ans += abs(5 - tmp) + 1
else:
    ans += tmp

print(ans)
