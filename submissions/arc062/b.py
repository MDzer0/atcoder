s = list(input())
y = [0] * (len(s))
cnt = 0
for i in range(len(s)):
    if s[i] == 'g':
        cnt += 1
    else:
        cnt -= 1

    y[i] = cnt

print(y[-1] // 2)
