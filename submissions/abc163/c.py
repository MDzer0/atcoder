N = int(input())
a = list(map(int, input().split()))
ans = [0] * N
for i in a:
    ans[i - 1] += 1

for i in ans:
    print(i)
