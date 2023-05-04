import copy

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
cs = copy.deepcopy(s)
for i in range(H):
    s[i].insert(0, '#')
    s[i].append('#')
add = ['#'] * (W + 2)
ad = ['.'] * (W + 2)
s.insert(0, add)
s.append(add)

ans = []
r = [1, 1, 1, 0, 0, -1, -1, -1]
c = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(1, H + 1):
    tmp = []
    for j in range(1, W + 1):
        shorF = True
        for k in range(8):
            if (s[i][j] == '#' and s[i + r[k]][j + c[k]] != '#')\
                    or s[i][j] == '.':
                shorF = False
                break
        if shorF:
            tmp.append('#')
        else:
            tmp.append('.')
    ans.append(tmp)

cpans = copy.deepcopy(ans)
for i in range(H):
    cpans[i].insert(0, '.')
    cpans[i].append('.')
cpans.insert(0, ad)
cpans.append(ad)

pos = []
for i in range(1, H + 1):
    tmp = []
    for j in range(1, W + 1):
        shorF = False
        for k in range(8):
            if cpans[i][j] == '#':
                shorF = True
                break
            if cpans[i][j] == '.' and cpans[i + r[k]][j + c[k]] == '#':
                shorF = True
                break
        if shorF:
            tmp.append('#')
        else:
            tmp.append('.')
    pos.append(tmp)

posibF = True
for i in range(H):
    for j in range(W):
      if pos[i][j] != cs[i][j]:
          print('impossible')
          exit()

print('possible')
for i in ans:
    for j in range(W):
        if j != W - 1:
            print(i[j], end='')
        else:
            print(i[j])
