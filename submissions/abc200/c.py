N = int(input())
A = list(map(int, input().split()))
tmp = [0] * 200

for i in A:
    tmp[i % 200] += 1

ans = 0
for i in tmp:
    ans += ((i * (i - 1)) // 2)

print(ans)
