b = list(map(int, input().split()))
N = int(input())
a = list(input() for _ in range(N))
ans = []
for i in range(N):
    tmp = ''
    for j in a[i]:
        for k in range(10):
            if int(j) == b[k]:
                tmp += str(k)
                break
    ans.append([i, int(tmp)])

ans.sort(key=lambda x: x[1])
for i in range(N):
    print(a[ans[i][0]])
