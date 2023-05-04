S = input()
ans = []
index = 0
while index <= len(S) - 1:
    if S[index] == '@':
        tmp = ''
        for i in range(index + 1, len(S)):
            if S[i] == '@' or S[i] == ' ':
                break
            tmp += S[i]
        if tmp != '':
            ans.append(tmp)
        index += len(tmp) + 1
    else:
        index += 1

ans = set(ans)
ans = list(ans)
ans.sort()
for i in ans:
    print(i)
