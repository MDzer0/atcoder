ilst = list(int(input()) for _ in range(5))
total = 0
if ilst[0] < 0:
    total += ilst[2] * abs(ilst[0])
    total += ilst[3]
    total += ilst[1] * ilst[4]
else:
    total += abs(ilst[0] - ilst[1]) * ilst[4]

print(total)
