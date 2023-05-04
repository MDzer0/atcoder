S = input()
slst = [[] for _ in range(len(S) + 1)]
tmp = S[0]
cnt = 0
index = 0
for i in range(len(S)):
    if tmp == S[i]:
        cnt += 1
    else:
        slst[index].append(tmp)
        slst[index].append(cnt)
        index += 1
        tmp = S[i]
        cnt = 1

slst[index].append(tmp)
slst[index].append(cnt)

dp = [0] * (len(S) + 1)
if slst[0][0] == '<':
    dp[0] = 0
else:
    dp[0] = slst[0][1]

index = 1
for i in range(len(S)):
    if slst[i] == []:
        break

    if slst[i][0] == '>':
        dp[index] = dp[index - 1] + ((slst[i][1]) * ((slst[i][1] - 1))) // 2
        index += 1
    else:
        if slst[i + 1] == []:
            dp[index] = dp[index - 1] + ((slst[i][1] + 1) * ((slst[i][1]))) // 2
            index += 1
        else:
            if slst[i][1] < slst[i + 1][1]:
                tdp = slst[i + 1][1]
                for k in range(1, slst[i][1]):
                    tdp += k
                dp[index] = dp[index - 1] + tdp
                index += 1

            else:
                dp[index] = dp[index - 1] + ((slst[i][1] + 1) * ((slst[i][1]))) // 2
                index += 1


print(dp[index - 1])
