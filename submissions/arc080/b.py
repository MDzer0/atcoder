H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
ans = [['' for i in range(W)] for i in range(H)]
indexH = 0
indexW = 0
cnt = 0
for i in range(N):
    for j in range(a[i]):
        ans[indexH][indexW] = i + 1
        if cnt % 2 == 0:
            if indexW == W - 1:
                indexW = -1
                indexH += 1
                cnt += 1
            else:
                indexW += 1
        else:
            if indexW == -W:
                indexW = 0
                indexH += 1
                cnt += 1
            else:
                indexW -= 1

for i in ans:
    print(*i)
