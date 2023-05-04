N, K = map(int, input().split())
cnt = 1
while True:
    N = N // K
    if N != 0:
        cnt += 1
    else:
        break
print(cnt)
