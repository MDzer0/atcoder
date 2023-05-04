N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

if K > sum(a):
    print(-1)
    exit()

cnt = 0
total = 0
for i in a:
    total += i
    cnt += 1
    if K <= total:
        break

print(cnt)
