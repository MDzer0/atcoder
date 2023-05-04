H, W = map(int, input().split())
s = [list('.' + input() + '.') for _ in range(H)]
alst = ['.'] * (W + 2)
s.insert(0, alst)
s.append(alst)

for i in range(1, H + 1):
    for j in range(1, W + 1):
        ansf = True
        if s[i][j] == '#':
            if s[i][j + 1] == '.' and s[i][j - 1] == '.' and\
                s[i - 1][j] == '.' and s[i + 1][j] == '.':
                  ansf = False
                  break
    if not ansf:
        print('No')
        exit()

print('Yes')
