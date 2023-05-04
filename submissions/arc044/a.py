N = int(input())
s = []
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        s.append(i)
        if i != N // i:
            s.append(N // i)

s.sort()
ans = 'Not Prime'

if len(s) == 2:
    ans = 'Prime'
elif len(s) != 1 and int(str(N)[-1]) % 2 != 0 and str(N)[-1] != '5':
    tmp = 0
    for i in range(len(str(N))):
        tmp += int(str(N)[i])
    if tmp % 3 != 0:
        ans = 'Prime'
print(ans)
