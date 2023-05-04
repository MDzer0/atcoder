import sys
input = sys.stdin.readline
S = input()
S = S[:-1]
ans = len(S) - 1
for i in range(1, len(S)):
    if S[i] == 'D':
        ans += i
        ans += (len(S) - 1 - i) * 2
    else:
        ans += i * 2
        ans += (len(S) - 1 - i)

print(ans)
