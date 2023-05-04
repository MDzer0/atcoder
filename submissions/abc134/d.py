N = int(input())
a = list(map(int, input().split()))
aN = 0
al = [0] * (N + 1)
ans = []
for i in reversed(range(1, N + 1)):
    total = 0
    for j in range(2 * i, N + 1, i):
        total += al[j]
    if total % 2 != a[i - 1]:
        al[i] = 1
        ans.append(i)
ans.reverse()
print(len(ans))
for i in ans:
    print(i, end=' ')
