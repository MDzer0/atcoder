N = int(input())
a = list(map(int, input().split()))
anslst = [0] * N

for i in range(N):
    anslst[a[i] - 1] = i + 1

for i in anslst:
    print(i, end=' ')

