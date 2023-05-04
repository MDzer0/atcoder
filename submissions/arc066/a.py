from collections import defaultdict

MOD = 10 ** 9 + 7
N = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)

for i in a:
    d[i] += 1

for v, c in d.items():
    if N % 2 == 0:
        if v % 2 == 1 and c == 2:
            continue
        else:
            print(0)
            exit()
    else:
        if v % 2 == 0 and c == 2:
            continue
        elif v == 0 and c == 1:
            continue
        else:
            print(0)
            exit()

print(pow(2, N // 2, MOD))
