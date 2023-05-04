S = input()
K = int(input())
for i in range(K):
    S = S[1:] + S[0:1]

print(S)
