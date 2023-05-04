N = int(input())
s = [input() for _ in range(N)]
rs = [''] * N
for i in range(N):
    rs[i] = s[i][::-1]

rs.sort()
ans = [''] * N
for i in range(N):
    ans[i] = rs[i][::-1]

for i in ans:
    print(i)
