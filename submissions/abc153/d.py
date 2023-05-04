H = int(input())

cnt = 1
H //= 2
tmp = 1
while H != 0:
    H //= 2
    cnt += 2 ** tmp
    tmp += 1
print(cnt)
