T = int(input())
N = int(input())
ninzu = [0] * (T + 1)

for i in range(N):
    l, r = map(int, input().split())
    ninzu[l] += 1
    ninzu[r] -= 1

for i in range(T):
    ninzu[i + 1] += ninzu[i]
print(*ninzu[:T])
