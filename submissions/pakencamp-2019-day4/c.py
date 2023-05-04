from bisect import bisect_left

lr = [list(map(int, input().split())) for _ in range(3)]
lr2 = [lr[1][0] + i for i in range(lr[1][1] - lr[1][0] + 1)]
lr3 = [lr[2][0] + i for i in range(lr[2][1] - lr[2][0] + 1)]
total = 1
for i in range(3):
    total *= lr[i][1] - lr[i][0] + 1
cnt = 0
for i in range(lr[0][0], lr[0][1] + 1):
    tmp1 = bisect_left(lr2, i + 1)
    tmp2 = bisect_left(lr3, i + 1)
    cnt += ((lr[1][1] - lr[1][0] + 1) - tmp1) * ((lr[2][1] - lr[2][0] + 1) - tmp2)

print(cnt / total)
