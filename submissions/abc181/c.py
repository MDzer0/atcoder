N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i):
        for k in range(j):
            x1 = xy[i][0]
            y1 = xy[i][1]
            x2 = xy[j][0]
            y2 = xy[j][1]
            x3 = xy[k][0]
            y3 = xy[k][1]
            x2 -= x1
            x3 -= x1
            y2 -= y1
            y3 -= y1
            if x2 * y3 == x3 * y2:
                print('Yes')
                exit()
                
print('No')
