K = int(input())
if K % 2 == 0 or K % 5 == 0:
    print(-1)
    exit()

tmp1 = 0
for i in range(1, K + 1):
    tmp1 += 7 * pow(10, i, K)
    if tmp1 % K == 0:
        print(i)
        exit()

print(-1)
