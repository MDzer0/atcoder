INF = 753
S = input()
ans = 9999999999
for i in range(len(S) - 2):
    ans = min(ans, abs((int(S[i:i + 3]) - INF)))
print(ans)
