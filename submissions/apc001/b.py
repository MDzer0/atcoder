N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = sum(b) - sum(a)
numa, numb = 0, 0
for i in range(N):
    if a[i] > b[i]:
        numb += a[i] - b[i]
    elif a[i] < b[i]:
        numa += (b[i] - a[i] + 1) // 2

if numa <= tmp and numb <= tmp:
    print('Yes')
else:
    print('No')
