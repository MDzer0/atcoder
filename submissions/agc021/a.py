N = input()
tmp1 = 0
tmp2 = 0

for i in range(len(N)):
    tmp1 += int(N[i])

tmp2 += int(N[0]) - 1
for i in range(len(N) - 1):
    tmp2 += 9

print(max(tmp1, tmp2))
