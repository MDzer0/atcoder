INF = 10 ** 6 + 1
sosu = [False] * INF

def era():
    sosu[0] = True
    sosu[1] = True
    for i in range(INF):
        if sosu[i]: continue
        for j in range(i * 2, INF, i):
            sosu[j] = True

N = int(input())
era()
for i in range(N + 1):
    if sosu[i] == False:
        print(i)
