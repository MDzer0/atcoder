import math

N = int(input())
nedan = math.floor(1.08 * N)

if nedan < 206:
    print('Yay!')
elif nedan == 206:
    print('so-so')
else:
    print(':(')
