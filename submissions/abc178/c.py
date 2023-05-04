N = int(input())
INF = 10 ** 9 + 7
print((pow(10, N, INF) - 2 * pow(9, N, INF) + pow(8, N, INF)) % INF)
