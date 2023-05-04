D, N = map(int, input().split())
anslst = [i for i in range(1, 100)]
anslst.append(101)
for i in range(N):
    anslst[i] = anslst[i] * 100 ** D

print(anslst[N - 1])
