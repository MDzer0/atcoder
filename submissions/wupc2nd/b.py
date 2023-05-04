N = int(input())
S = input()

cnt = 0
tmp = 0
ans = 0
while cnt < N:
    if S[cnt] == '.':
        tmp = 0
    else:
        if tmp == 2:
            ans += 1
            tmp = 0
        else:
            tmp += 1
    cnt += 1
print(ans)
