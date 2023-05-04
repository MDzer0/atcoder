D = int(input())
N = int(input())
sanka = [0] * (D + 2)

for i in range(N):
    l, r = map(int, input().split())
    sanka[l] += 1
    sanka[r + 1] -= 1

for i in range(D):
    sanka[i + 1] += sanka[i]

for i in range(D):
    print(sanka[i + 1])
