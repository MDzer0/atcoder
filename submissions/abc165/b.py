X = int(input())
cnt = 1
t = 100
while True:
    t = int(t * 1.01)
    if X <= t:
        print(cnt)
        exit()
    else:
        cnt += 1
