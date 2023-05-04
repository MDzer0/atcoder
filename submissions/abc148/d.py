N = int(input())
a = list(map(int, input().split()))
ans = -1

if a.count(1) == 0:
    print(ans)
    exit()

index = 1
for i in range(N):
    if a[i] == index:
        index += 1

print(N - (index - 1))
