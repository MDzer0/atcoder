import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
ki =[[] for _ in range(N)]
ab = []
dict = {}
k = 0
def dfs(v, p = 0, ban_color = 0):
    global k
    color = 1
    for i in ki[v]:
        if i == p:
            continue
        if ban_color == color:
            color += 1
        dict[(v, i)] = color
        dfs(i, v, color)
        color += 1
    k = max(k, color - 1)
    return


for i in range(N - 1):
    a, b = map(int, input().split())
    ki[a - 1].append(b - 1)
    ki[b - 1].append(a - 1)
    ab.append((a - 1, b - 1))

dfs(0)
print(k)
for key in ab:
    print(dict[key])
