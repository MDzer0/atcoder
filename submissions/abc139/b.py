import sys
A, B = map(int, input().split())
tmp = A
ans = 1
if B == 1:
    print(0)
    sys.exit()

while True:
    if A < B:
        A += tmp - 1
        ans += 1
    else:
        break

print(ans)
