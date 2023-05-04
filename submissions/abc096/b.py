A, B, C = map(int, input().split())
K = int(input())

editlist = [A, B, C]
editlist.sort(reverse=True)

for i in range(K):
    editlist[0] = editlist[0] * 2
ans = 0
for i in editlist:
    ans += i
print(ans)
