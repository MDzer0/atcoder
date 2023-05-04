def check(n):
    return n ** 3 + n

N = int(input())

down = 0
up = 100

for i in range(20):
    mid = (up + down) / 2
    if check(mid) > N:
        up = mid
    else:
        down = mid

print(up)
