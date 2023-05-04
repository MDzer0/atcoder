import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
h = [list(map(int, input().split())) for _ in range(N)]
sh = sorted(h, key=lambda x: x[2], reverse=True)

ans = [0] * 3
for i in range(101):
    for j in range(101):
        ansB = True
        ansh = sh[0][2] + abs(sh[0][0] - i) + abs(sh[0][1] - j)
        for k in range(N):

            tmp = max(ansh - abs(sh[k][0] - i) - abs(sh[k][1] - j), 0)

            if tmp != sh[k][2]:
                ansB = False
                break

        if ansB:
            print(i, j, ansh)
            sys.exit()

