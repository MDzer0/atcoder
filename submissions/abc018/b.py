S = input()
N = int(input())
nlst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    S = S[:nlst[i][0] - 1] + S[nlst[i][0] - 1: nlst[i][1]][::-1] + S[nlst[i][1]:]
print(S)
