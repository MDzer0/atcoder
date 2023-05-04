S = input()
cnt = 0
def dfs():
    global cnt
    addS = ''

    while cnt < len(S):
        if S[cnt] == '(':
            cnt += 1
            addS += dfs()
        elif S[cnt] == ')':
            cnt += 1
            addS += addS[::-1]
            break
        else:
            addS += S[cnt]
            cnt += 1
    return addS

print(dfs())
