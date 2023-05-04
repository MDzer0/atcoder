N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
total = a[0]
index = 1
cnt = 0
for i in range(N - 2):
    if cnt == 2:
        index += 1
        cnt = 0
    total += a[index]
    cnt += 1

print(total)
