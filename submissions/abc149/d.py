N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
ans = 0
dic = {'r': P, 's': R, 'p': S}
tmp = [''] * (N + 1)
for i in range(K):
    ans += dic[T[i]]
    tmp[i] = T[i]

for i in range(K, N):
    if T[i] != tmp[i - K]:
        ans += dic[T[i]]
        tmp[i] = T[i]
    else:
        tmp[i] = 't'
print(ans)
