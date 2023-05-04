N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(1, N - 1):
    cnt1 = 0
    for j in range(0, i):
        if A[j] < A[i]:
            cnt1 += 1

    cnt2 = 0
    for j in range(i + 1, N):
        if A[j] < A[i]:
            cnt2 += 1
    ans += cnt1 * cnt2
print(ans)
