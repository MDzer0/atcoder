N = int(input())
S = [input() for _ in range(N)]
ans_list = []

for i in range(N):
    for j in range(i + 1, N):
        ans_list.append(S[i] + S[j])
        ans_list.append(S[j] + S[i])

ans_list.sort()
print(ans_list[0])
