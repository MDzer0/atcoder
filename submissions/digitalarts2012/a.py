s = list(input().split())
N = int(input())
err = [input() for _ in range(N)]

for i in range(len(s)):
    for j in err:
        errF = True
        if len(s[i]) == len(j):
            for k in range(len(j)):
                if s[i][k] == j[k] or j[k] == '*':
                    continue
                else:
                    errF = False
                    break
        else:
            errF = False
        if errF:
            s[i] = '*' * len(j)

print(*s, end=' ')
