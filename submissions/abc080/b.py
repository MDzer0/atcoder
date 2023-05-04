N = input()
total = 0

for i in range(len(N)):
    total += int(N[i])

if int(N) % total == 0:
    print('Yes')
else:
    print('No')
