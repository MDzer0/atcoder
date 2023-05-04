import sys

h, m = map(int, input().split())
tmph = 18
tmpm = 60
ans = 0

if m != 00:
    ans = (tmph - 1 - h) * 60
else:
    ans = (tmph - h) * 60
    print(ans)
    sys.exit()

ans += (tmpm - m)
print(ans)
