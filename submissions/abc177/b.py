S = input()
T = input()

cnt = 10 ** 9
for i in range(len(S) - len(T) + 1):
    tmp = 0
    for j in range(len(T)):
        if i + j < len(S) and S[i + j] == T[j]:
            continue
        else:
            tmp += 1
    cnt = min(cnt, tmp)

print(cnt)
