import sys
sys.setrecursionlimit(10**6)

def dfs(index):
    global ans
    global deep
    while index < len(S):
        if S[index] == '{':
            deep += 1
            index = dfs(index + 1)
        elif S[index] == '}':
            deep -= 1
            return index + 1
        elif S[index] == ':' and deep == 1:
            ans = 'dict'
            index += 1
        else:
            index += 1
    return

S = input()
if S == '{}':
    print('dict')
    exit()

ans = 'set'
deep = 0
dfs(0)

print(ans)
