N = int(input())
s = [''] * N
for _ in range(N):
    tmp = sorted(input())
    s[_] = ''.join(tmp)
tmp = sorted(s)
cnt = 1
index = 0
ansFlag = True
ans1 = 0
while ansFlag:
    cnt = 1
    for j in range(index + 1, N):
        if tmp[index] == tmp[j]:
            cnt += 1
            index += 1
        else:
            index += 1
            break

    tmp2 = 0
    for i in range(cnt, 0, -1):
        tmp1 = i - 1
        tmp2 += tmp1
        ans = tmp2
    ans1 += ans
    if index == (N - 1):
        ansFlag = False

print(ans1)
