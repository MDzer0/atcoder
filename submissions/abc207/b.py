A, B, C, D = map(int, input().split())
cnt = 0
tmpC = 0
for i in range(1, A + 1):
    cnt += 1
    A += B
    tmpC += C
    if A <= D * tmpC:
        print(cnt)
        exit()

print(-1)
