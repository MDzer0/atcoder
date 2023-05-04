S, P = map(int, input().split())
for i in range(1, int(pow(P, 0.5)) + 1):
    m, d = divmod(P, i)
    if d == 0:
        if i + m == S:
            print('Yes')
            exit()
print('No')
