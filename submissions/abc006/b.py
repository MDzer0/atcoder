import sys
INF = 10007
n = int(input())
ansLst = [0] * n

if n == 1 or n == 2:
    print(0)
    sys.exit()
elif n == 3:
    print(1)
    sys.exit()
ans = 0
ansLst[2] = 1
for i in range(3, n):
    ansLst[i] = (ansLst[i - 1] + ansLst[i - 2] + ansLst[i - 3]) % INF

print(ansLst[-1])
