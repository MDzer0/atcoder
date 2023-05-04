from decimal import *
D, W = map(int, input().split())
ans = []
D = D / 10
if 11.25 <= D < 33.75:
    ans.append('NNE')
elif 33.75 <= D < 56.25:
    ans.append('NE')
elif 56.25 <= D < 78.75:
    ans.append('ENE')
elif 78.75 <= D < 101.25:
    ans.append('E')
elif 101.25 <= D < 123.75:
    ans.append('ESE')
elif 123.75 <= D < 146.25:
    ans.append('SE')
elif 146.25 <= D < 168.75:
    ans.append('SSE')
elif 168.75 <= D < 191.25:
    ans.append('S')
elif 191.25 <= D < 213.75:
    ans.append('SSW')
elif 213.75 <= D < 236.25:
    ans.append('SW')
elif 236.25 <= D < 258.75:
    ans.append('WSW')
elif 258.75 <= D < 281.25:
    ans.append('W')
elif 281.25 <= D < 303.75:
    ans.append('WNW')
elif 303.75 <= D < 326.25:
    ans.append('NW')
elif 326.25 <= D < 348.75:
    ans.append('NNW')
else:
    ans.append('N')
W = float(Decimal(str(W / 60)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))

if 0.0 <= W <= 0.2:
    ans.append(0)
elif 0.3 <= W <= 1.5:
    ans.append(1)
elif 1.6 <= W <= 3.3:
    ans.append(2)
elif 3.4 <= W <= 5.4:
    ans.append(3)
elif 5.5 <= W <= 7.9:
    ans.append(4)
elif 8.0 <= W <= 10.7:
    ans.append(5)
elif 10.8 <= W <= 13.8:
    ans.append(6)
elif 13.9 <= W <= 17.1:
    ans.append(7)
elif 17.2 <= W <= 20.7:
    ans.append(8)
elif 20.8 <= W <= 24.4:
    ans.append(9)
elif 24.5 <= W <= 28.4:
    ans.append(10)
elif 28.5 <= W <= 32.6:
    ans.append(11)
else:
    ans.append(12)
if ans[1] == 0:
    ans[0] = 'C'

print(ans[0], ans[1])
