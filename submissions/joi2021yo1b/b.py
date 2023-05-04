N = int(input())
S = input()

ans = 'No'
for i in range(N - 2):
    if S[i] != 'I': continue
    for j in range(i, N - 1):
        if S[j] != 'O': continue
        for k in range(j, N):
            if S[k] == 'I':
                print('Yes')
                exit()

print(ans)
