m1 = float(input())
m2 = m1 / 1000
ans = 0
if m2 < 0.1:
    ans = '00'
elif m2 >= 0.1 and m2 <= 0.9:
    m2 = int(m2*10)
    ans = '0' + str(m2)
elif m2 >= 1 and  m2 <= 5:
    ans =int(m2 * 10)
elif m2 >= 6 and m2 <= 30:
    ans = int(m2 + 50)
elif m2 >= 35 and m2 <= 70:
    ans = int(((m2 - 30) / 5) + 80)
else:
    ans = 89
print(ans)
