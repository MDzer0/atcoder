S = input()
ans = int(S[0])

for i in range(1, len(S)):
    if i % 2 == 0:
        ans += int(S[i])
    else:
        ans -= int(S[i])

print(ans)
