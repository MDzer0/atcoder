N = int(input())
S = input()
ansJuge = False

for i in range(N - 2):
    if S[i] == 'R' and S[i + 1] == 'R' and S[i + 2] == 'R':
        ansJuge = True
        break
    elif S[i] == 'B' and S[i + 1] == 'B' and S[i + 2] == 'B':
        ansJuge = True
        break

if ansJuge:
    print('Yes')
else:
    print('No')
