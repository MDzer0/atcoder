N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(1, N + 1):
    cnt = 1
    index = i - 1
    while True:
        if A[index] == i:
            ans.append(cnt)
            break
        else:
            cnt += 1
            index = A[index] - 1

print(*ans)
