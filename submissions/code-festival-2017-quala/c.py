import string
H, W = map(int, input().split())
a = [input() for _ in range(H)]
abc = string.ascii_lowercase
cnt = [0] * 26
cnt4 = [0] * 4
for i in a:
    for j in i:
        cnt[abc.index(j)] += 1

for i in cnt:
    if i == 0: continue
    cnt4[i % 4] += 1

if H % 2 == 0 and W % 2 == 0:
    for i in range(1, 4):
        if cnt4[i] != 0:
            print('No')
            exit()
    print('Yes')
    exit()

if H % 2 == 1 and W % 2 == 1:
    if cnt4[3]:
        print('No')
        exit()
    if cnt4[1] != 1:
        print('No')
        exit()
    if cnt4[2] > H + W - 1:
        print('No')
        exit()
    print('Yes')
    exit()

if cnt4[1] or cnt4[3]:
    print('No')
    exit()

tmp = 0
if W % 2 == 0:
    tmp = W
else:
    tmp = H
if cnt4[2] > tmp // 2:
    print('No')
    exit()

print('Yes')
