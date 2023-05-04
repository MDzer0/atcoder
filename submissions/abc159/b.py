S = input()
S1 = S[:(len(S) - 1) // 2:]
S2 = S[(len(S) + 3) // 2 - 1:]

ans = 'Yes'
for i in range(len(S) // 2 + 1):
    if S[i] != S[-i - 1]:
        ans = 'No'
        print(ans)
        exit()

for i in range((len(S1) // 2) + 1):
    if S1[i] != S1[-i - 1]:
        ans = 'No'
        print(ans)
        exit()

for i in range(len(S2) // 2 + 1):
    if S2[i] != S2[-i - 1]:
        ans = 'No'
        print(ans)
        exit()

print(ans)
