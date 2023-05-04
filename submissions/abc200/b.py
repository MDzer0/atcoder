N, K = input().split()
tmp = N
for i in range(int(K)):
    tmp = int(tmp)
    if tmp % 200 == 0:
        tmp //= 200
        tmp = str(tmp)
    else:
        tmp = str(tmp) + '200'

print(tmp)
