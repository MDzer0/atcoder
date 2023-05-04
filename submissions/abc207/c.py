N = int(input())
lr = [list(map(int, input().split())) for _ in range(N)]
lr.sort(key=lambda x: x[2])
ans = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        if lr[i][2] >= lr[j][1]:
            if lr[i][2] == lr[j][1]:
                if (lr[i][0] == 1 or lr[i][0] == 3)\
                        and (lr[j][0] == 1 or lr[j][0] == 2):
                    ans += 1
            else:
                ans += 1

print(ans)
