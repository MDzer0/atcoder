N = int(input())
a = list(map(int, input().split()))
ans = [0] * (2 ** N)

for i in range(N):
    cnt = 0
    tmp = -1
    for j in range(2 ** N):
        if ans[j] == 0 and cnt == 0:
            cnt += 1
            tmp = j
        elif ans[j] == 0 and cnt == 1:
            cnt = 0
            if a[tmp] < a[j]:
                ans[tmp] = i + 1
            else:
                ans[j] = i + 1

for i in ans:
    if i == 0:
        print(N)
    else:
        print(i)
