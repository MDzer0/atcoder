N, K = input().split()
if int(K) == 0:
    print(int(N))
    exit()

ans = list(N)

for i in range(int(K)):
    g1 = sorted(ans, reverse=True)
    sg1 = ''
    for j in g1:
        sg1 += j
    g2 = sorted(ans)
    sg2 = ''
    for j in g2:
        sg2 += j

    ans = str(int(sg1) - int(sg2))
print(int(ans))
