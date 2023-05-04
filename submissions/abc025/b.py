N, A, B = map(int, input().split())
sLst = [list(map(str, input().split())) for i in range(N)]
ans = 0

for i in range(N):
    if int(sLst[i][1]) < A:
        if sLst[i][0] == 'East':
            ans -= A
        else:
            ans += A
    elif A <= int(sLst[i][1]) and int(sLst[i][1]) <= B:
        if sLst[i][0] == 'East':
            ans -= int(sLst[i][1])
        else:
            ans += int(sLst[i][1])
    else:
        if sLst[i][0] == 'East':
            ans -= B
        else:
            ans += B

if ans > 0:
    print('West', ans)
elif ans < 0:
    print('East', abs(ans))
else:
    print(0)
