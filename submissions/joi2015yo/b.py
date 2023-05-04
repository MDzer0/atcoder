N = int(input())
M = int(input())
a = list(map(int, input().split()))
ans = [0] * N
for i in range(M):
    touhyo = list(map(int, input().split()))
    cnt = 0
    for j in range(N):
        if a[i] == touhyo[j]:
            ans[j] += 1
            cnt += 1
    ans[a[i] - 1] += N - cnt

for i in ans:
    print(i)
