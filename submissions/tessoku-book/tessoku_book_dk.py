N = int(input())
S = list(input())
AnsList = [1] * N

cnt = 1
for i in range(N - 1):
    if S[i] == 'A':
        cnt += 1
    else:
        cnt = 1
    AnsList[i + 1] = cnt

cnt = 1
for i in reversed(range(N - 1)):
    if S[i] == 'B':
        cnt += 1
    else:
        cnt = 1
    AnsList[i] = max(cnt, AnsList[i])
print(sum(AnsList))
