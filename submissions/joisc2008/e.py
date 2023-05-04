N = int(input())
A = [0] * N
par = [0] * N
child = [[] for i in range(N)]
num_children = [0] * N
leaf = set(range(N))

for i in range(N):
    s, a = map(int, input().split())
    par[i] = s - 1; A[i] = a
    leaf.discard(s - 1)
    if i:
        num_children[s - 1] += 1
        child[s - 1].append(i)

score = [-100] * N
d = list(leaf)
ans = -100
while d:
    i = d.pop()
    children = child[i]
    score_i = sum(score[c] if score[c]>0 else 0 for c in children) + A[i]
    score[i] = score_i
    ans = max(ans, score_i)
    num_children[par[i]] -= 1
    if num_children[par[i]] == 0:
        d.append(par[i])

print(ans)
