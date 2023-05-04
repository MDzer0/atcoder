N = int(input())
cnt = 0
while True:
    tmp = int(pow(N, 0.5))
    if N == tmp ** 2:
        break
    else:
        N += 1
        cnt += 1

print(cnt)
