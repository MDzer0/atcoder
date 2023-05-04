A, B = map(int, input().split())

for i in range(A, B + 1):
    d, m = divmod(100, i)
    if m == 0:
        print('Yes')
        exit()

print('No')
