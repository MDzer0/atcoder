import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

M, D = map(int, input().split())

ans = 0
for i in range(1, M + 1):
    for j in range(2, (D // 10) + 1):
        for k in range(2, 10):
            tmp = int(str(j) + str(k))
            if D < tmp:
                break
            if i == j * k:
                ans += 1

print(ans)
