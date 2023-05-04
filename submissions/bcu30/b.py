from collections import defaultdict

s = [list(input()) for _ in range(9)]

for i in range(9):
    d = defaultdict(int)
    for j in s[i]:
        d[j] += 1
    for v, m in d.items():
        if m > 1:
            print('No')
            exit()

for i in range(9):
    d = defaultdict(int)
    for j in range(9):
        d[s[j][i]] += 1
    for v, m in d.items():
        if m > 1:
            print('No')
            exit()

for i in range(9):
    for j in range(9):
        d = defaultdict(int)
        if i >= 1 and j >= 2:
            d[s[i - 1][j - 2]] += 1
        if i >= 2 and j >= 1:
            d[s[i - 2][j - 1]] += 1
        if i <= 7 and j >= 2:
            d[s[i + 1][j - 2]] += 1
        if i <= 6 and j >= 1:
            d[s[i + 2][j - 1]] += 1
        if i <= 7 and j <= 6:
            d[s[i + 1][j + 2]] += 1
        if i <= 6 and j <= 7:
            d[s[i + 2][j + 1]] += 1
        if i >= 1 and j <= 6:
            d[s[i - 1][j + 2]] += 1
        if i >= 2 and j <= 7:
            d[s[i - 2][j + 1]] += 1
        d[s[i][j]] += 1
        if d[s[i][j]] != 1:
            print('No')
            exit()
print('Yes')
