N, C = input().split()
A = input()

score = 0
for i in A:
    if i == 'B':
        score += 1
    elif i == 'R':
        score += 2

tmp = score % 3
if tmp == 0 and C == 'W':
    print('Yes')
elif tmp == 1 and C == 'B':
    print('Yes')
elif tmp == 2 and C == 'R':
    print('Yes')
else:
    print('No')
