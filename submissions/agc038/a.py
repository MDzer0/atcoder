H, W, A, B = map(int, input().split())
zerone = [0, 1]
ans = []

for i in range(H):
    gyo = [0] * W
    if i < B:
        for j in range(W):
            if j >= A:
                gyo[j] = 1
        ans.append(gyo)
    else:
        for j in range(W):
            if j < A:
                gyo[j] = 1
        ans.append(gyo)

for i in ans:
    for j in i:
        print(j, end='')
    print()
