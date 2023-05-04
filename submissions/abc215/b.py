N = int(input())
cnt = 0
while N >= 2 ** cnt:
    cnt += 1

print(cnt - 1)
