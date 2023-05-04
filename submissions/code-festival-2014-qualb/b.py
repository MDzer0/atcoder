N, K = map(int, input().split())
a = list(int(input()) for _ in range(N))
total = 0
cnt = 0
for i in a:
    total += i
    cnt += 1
    if total >= K:
        print(cnt)
        exit()
