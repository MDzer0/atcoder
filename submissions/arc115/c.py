import bisect

N = int(input())
yakusu = []
cnt = 1
while cnt < N + 1:
    yakusu.append(cnt)
    cnt *= 2

len_yakusu = len(yakusu)
ans = []
v = 0
for i in range(1, N + 1):
    index = bisect.bisect_left(yakusu, i)
    if index < len_yakusu:
        if yakusu[index] == i:
            v += 1
    ans.append(v)

print(*ans)
