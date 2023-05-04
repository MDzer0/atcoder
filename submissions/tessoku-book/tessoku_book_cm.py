import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
harf = N // 2
hList = []

for i in range(1 << harf):
    tmp = 0
    for j in range(harf):
        if i >> j & 1:
            tmp += A[j]
    hList.append(tmp)
hList.sort()

for i in range(1 << (N - harf)):
    tmp = 0
    for j in range((N - harf)):
        if i >> j & 1:
            tmp += A[harf + j]
    index = bisect.bisect_left(hList, K - tmp)
    if index < len(hList) and hList[index] + tmp == K:
        print('Yes')
        exit()
print('No')
