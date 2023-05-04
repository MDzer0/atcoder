C = int(input())
nml = [list(map(int, input().split())) for _ in range(C)]

for i in range(C):
    nml[i].sort()

n, m, l = 0, 0, 0
for i in nml:
    n = max(n, i[0])
    m = max(m, i[1])
    l = max(l, i[2])

print(n * m * l)
