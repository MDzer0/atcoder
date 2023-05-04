N = int(input())
al = [list([0] * 2) for _ in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    al[i][0] = a
    al[i][1] = b
al.sort(key=lambda x:(x[1], x[0]))
ans = 'Yes'
t = 0
for i in range(N):
    t += al[i][0]
    if t > al[i][1]:
        ans = 'No'
        break

print(ans)
