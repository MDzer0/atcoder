S = input()
ans = 0
for i in range(len(S)):
    tmp = 0
    for j in range(len(S)):
        if 'ACGT'.count(S[j]) == 1:
            tmp += 1
            ans = max(ans, tmp)
        else:
            tmp = 0

print(ans)
