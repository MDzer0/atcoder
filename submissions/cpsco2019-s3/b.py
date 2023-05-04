N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt = 0
total = 0
for i in a:
    cnt += 1
    total += i
    if M <= total:
        break

print(cnt)
