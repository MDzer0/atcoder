N, L = map(int, input().split())
AB = [list(input().split()) for _ in range(N)]
ans = 0
for i in range(N):
    if AB[i][1] == 'E':
        ans = max(ans, L - int(AB[i][0]))
    else:
        ans = max(ans, int(AB[i][0]))
print(ans)
