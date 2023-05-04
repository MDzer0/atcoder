from collections import defaultdict

N, M = map(int, input().split())
name = input()
kit = input()
dictk = defaultdict(int)
for i in kit:
    dictk[i] += 1

dictn = defaultdict(int)
for i in name:
    dictn[i] += 1

ans = 0
for v, c in dictn.items():
    if dictk[v] == 0:
        ans = -1
        break
    else:
        if c >= dictk[v]:
            if c % dictk[v] == 0:
                ans = max(ans, c // dictk[v])
            else:
                ans = max(ans, c // dictk[v] + 1)
        else:
            ans = max(1, ans)

print(ans)
