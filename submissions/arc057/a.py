TYO = 2 * (10 ** 12)
A, K = map(int, input().split())
cnt = 0
tmp = A

if K == 0:
    print(TYO - A)
    exit()

while True:
    if tmp >= TYO:
        break
    tmp += tmp * K + 1
    cnt += 1
print(cnt)
