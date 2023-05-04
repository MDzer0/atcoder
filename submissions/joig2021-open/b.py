N, K = map(int, input().split())
T = input()

oomoji = ['J', 'O', 'I']
komoji = ['j', 'o', 'i']
ans = T[:K - 1]
for i in range(K - 1, N):
    for j in range(3):
        if T[i] == oomoji[j]:
            ans += komoji[j]
            break

    for j in range(3):
        if T[i] == komoji[j]:
            ans += oomoji[j]
            break

print(ans)
