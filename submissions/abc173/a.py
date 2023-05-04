N = int(input())
cnt = 0
m, d = divmod(N, 1000)
if d == 0:
    print(0)
else:
    print(1000 - d)
