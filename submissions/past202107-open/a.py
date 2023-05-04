S = input()
check = 0
for i in range(0, len(S) - 1, 2):
    check += int(S[i])
check *= 3

for i in range(1, len(S), 2):
    check += int(S[i])

check %= 10

if check == int(S[-1]):
    print('Yes')
else:
    print('No')
