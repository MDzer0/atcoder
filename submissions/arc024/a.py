L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
l.sort(), r.sort()

cnt = 0
for i in range(len(r)):
    for j in range(len(l)):
        if r[i] == l[j]:
            cnt += 1
            l.pop(j)
            break

        if r[i] < l[j]:
            break

print(cnt)
