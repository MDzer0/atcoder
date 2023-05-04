A, B, W = map(int, input().split())
ans = 'UNSATISFIABLE'
W = W * 1000
maxans = -1
minans = 10 ** 20

for i in range(1, W + 1):
    if A * i <= W <= B * i:
        maxans = max(maxans, i)
        minans = min(minans, i)

if minans == 10 ** 20:
    print(ans)
else:
    print(minans, maxans)
