S = list(map(str, input().split()))
ans = []
for i in range(len(S)):
    if S[i] == 'Left':
        ans.append('<')
    elif S[i] == 'Right':
        ans.append('>')
    else:
        ans.append('A')

print(*ans)
