abc = list(map(int, input().split()))
abc.sort(reverse=True)
ans = 0
tmp = abc[0]
for i in range(1, 3):
    ans += tmp - abc[i]

print(ans)
