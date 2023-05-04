S = input()
ans = 0
for i in range(1, len(S)):
    tmpI = (len(S) - i) // 2
    if S[:tmpI] == S[tmpI:len(S) - i]:
        ans = len(S) - i
        break

print(ans)
