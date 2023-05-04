N = int(input())
tokuten = [[i, int(input())] for i in range(N)]
tokuten.sort(key=lambda x:x[1], reverse=True)
ans = [0] * N
index = 0
tmp = 0
cnt = 0
for i in range(N):
    if tokuten[i][1] != tmp:
        index += 1 + cnt
        cnt = 0
        ans[tokuten[i][0]] = index
        tmp = tokuten[i][1]
    else:
        cnt += 1
        ans[tokuten[i][0]] = index

for i in ans:
    print(i)
