N = int(input())
A = input()
B = input()
C = input()
wordlst = [A, B, C]
cnt = 0
for i in range(N):
    tmp = 0
    for j in range(3):
        tmp += wordlst[j - 1][i].count(wordlst[j][i])
        tmp += wordlst[j - 2][i].count(wordlst[j][i])
    if tmp == 0:
        cnt += 2
    elif tmp == 2:
        cnt += 1

print(cnt)
