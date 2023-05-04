import itertools
import math
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
waru = math.factorial(N)
ans = 0
total = 0
for i in itertools.permutations(xy, N):
    for j in range(1, N):
        total += ((i[j - 1][0] - i[j][0]) ** 2 + (i[j - 1][1] - i[j][1]) ** 2) ** 0.5

print(total / waru)
