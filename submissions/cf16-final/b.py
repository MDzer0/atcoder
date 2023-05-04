N = int(input())
ans = 0

if N < 3:
    print(N)
    exit()

for i in range(1, N + 1):
    tmp = (i * (i - 1)) //  2
    if tmp >= N:
        ans = i - 1
        break

anslst = [i for i in range(ans, 0, -1)]
tmp = N - anslst[0]
print(anslst[0])
for i in anslst[1:]:
    if tmp - i < 0:
        continue
    if tmp == 0:
        break
    print(i)
    tmp -= i
