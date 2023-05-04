N = int(input())
a = list(map(int, input().split()))
a.sort()
pea = []
for i in range(N // 2):
    pea.append(a[i] + a[-i - 1])
pea.sort()

print(pea[-1] - pea[0])
