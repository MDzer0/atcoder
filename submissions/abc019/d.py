N = int(input())
p = 1
kyori = 0
for i in range(1, N):
    print('?', 1, i + 1)
    tmp = int(input())
    if kyori < tmp:
        kyori = tmp
        p = i + 1

ans = 0
for i in range(1, N + 1):
    print('?', p, i)
    tmp = int(input())
    if ans < tmp:
        ans = tmp

print('!', ans)
