h = list(map(int, input().split()))
m = list(map(int, input().split()))
s = list(map(int, input().split()))
hms = [h, m, s]
for i in range(3):
    tmp = [0] * 3
    sage = 0
    if hms[i][5] < hms[i][2]:
        sage = 1
    tmp[2] = (hms[i][5] - hms[i][2]) % 60
    if (hms[i][4] - sage) % 60 < hms[i][1]:
        tmp[1] = (hms[i][4] - sage - hms[i][1]) % 60
        sage = 1
    else:
        tmp[1] = (hms[i][4] - sage - hms[i][1]) % 60
        if sage == 1 and (hms[i][4] - sage) % 60 == 59:
            sage = 1
        else:
            sage = 0
    tmp[0] = hms[i][3] - sage - hms[i][0]
    print(*tmp)
