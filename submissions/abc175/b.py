import itertools

N = int(input())
L = list(map(int, input().split()))
cnt = 0

for i in itertools.combinations(L, 3):
    if i[0] != i[1] and i[0] != i[2] and i[2] != i[1]:
        if i[0] + i[1] > i[2] and i[1] + i[2] > i[0] and i[2] + i[0] > i[1]:
            cnt += 1


print(cnt)
