N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = N * M * B
ans += sum(A) * M + sum(C) * N
print(ans)
