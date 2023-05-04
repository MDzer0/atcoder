from collections import defaultdict
import string

N = int(input())
tmp = N // 2
S = [input() for _ in range(N)]
ans = ''

for i in range(tmp):
    zen = defaultdict(int)
    kou = defaultdict(int)
    for j in range(N):
        zen[S[i][j]] += 1
        kou[S[N - 1 - i][j]] += 1
    for j in string.ascii_lowercase:
        if j in zen and j in kou:
            ans += j
            break

if len(ans) == tmp:
    if N % 2 == 1:
        print(ans + S[tmp][0] + ans[::-1])
    else:
        print(ans + ans[::-1])
else:
    print(-1)
