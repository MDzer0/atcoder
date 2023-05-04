import sys
X, Y = map(int, input().split())
if X % Y == 0:
    print(-1)
    sys.exit()

for i in range(2, 10 ** 18 + 1):
    ans = i * X
    if ans % Y != 0:
        print(ans)
        sys.exit()
