T = int(input())
for i in range(T):
    l, r = map(int, input().split())
    tmp = r - l * 2
    if tmp < 0:
        print(0)
        continue
    print(((tmp + 1) * (tmp + 2)) // 2)
