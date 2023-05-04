S = input()
index = 0
cnt = 0
ans = 0

while index < len(S) - 1:
    if S[index] == '2' and S[index + 1] == '5':
        cnt += 1
        index += 2
    else:
        ans += ((cnt + 1) * cnt) // 2
        index += 1
        cnt = 0
if cnt != 0:
    ans += ((cnt + 1) * cnt) // 2
print(ans)
