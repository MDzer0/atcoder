X, Y = map(int, input().split())
ans = 'No'
for i in range(X + 1):
    cnt = (i * 2) + ((X - i) * 4)
    if cnt == Y:
        print('Yes')
        exit()
print(ans)
