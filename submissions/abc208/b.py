P = int(input())
cin_list = [0] * 11
cnt = 1
for i in range(1, 11):
    cnt *= i
    cin_list[i] = cnt

ans = 0
for i in reversed(range(11)):
    m, d = divmod(P, cin_list[i])
    ans += m
    P = d
    if P == 0:
        break
print(ans)
