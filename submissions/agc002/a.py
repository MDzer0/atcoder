import sys

a, b = map(int, input().split())
cnt = 0
if a <= 0 and 0 < b:
    print('Zero')
    sys.exit()

if b <= 0:
    cnt = abs(a - b) + 1

ans = ''
if cnt % 2 == 0:
    ans = 'Positive'
else:
    ans = 'Negative'

print(ans)
