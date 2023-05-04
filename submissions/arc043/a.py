N, A, B = map(int, input().split())
s = [int(input()) for _ in range(N)]
s.sort()
tmp = s[-1] - s[0]
if tmp == 0:
    print(-1)
    exit()

ave = sum(s) / N
P = B / tmp
Q = A - P * ave
print(P, Q)
