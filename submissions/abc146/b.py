import string

N = int(input())
S = input()
tmp = [''] * len(S)

for i in range(len(S)):
    tmp[i] = string.ascii_uppercase.index(S[i])

ans = ''
for i in tmp:
    ans += string.ascii_uppercase[(i + N) % 26]
print(ans)
