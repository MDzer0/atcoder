S = input()

loop = True
index = 1
ans = 1
stmp = S[0]
cnt = 1
while loop:
    if index == len(S):
        break
    if stmp == S[cnt: index + 1]:
        index += 1
        continue
    else:
        ans += 1
        index += 1
        stmp = S[cnt: index]
        cnt = index
print(ans)
