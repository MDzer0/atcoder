N = int(input())
p = list(map(int, input().split()))
ilist = [0] * N
for i in range(N):
    ilist[p[i] - 1] = i
s = ilist[N - 1]
cnt = 0
index = N - 1
ans = []
while cnt < N - 1:
    if index < 0:
        break
    if s == index:
        index -= 1
        s = ilist[index]
        continue
    cnt += 1
    ans.append(s + 1)
    tmp = p[s + 1]
    p[s + 1] = p[s]
    p[s] = tmp
    ilist[index] += 1
    ilist[p[s] - 1] -= 1
    s = ilist[index]

if cnt != N - 1:
    print(-1)
else:
    for i in range(N):
        if p[i] != i + 1:
            print(-1)
            exit()
    for i in ans:
        print(i)
