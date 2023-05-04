while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    x = list(map(int, input().split()))
    x.sort()

    cnt = 0
    total = 0
    for i in x:
        total += i
        cnt += 1
        if cnt == k:
            print(total)
            break
