import bisect

N = int(input())
a = [int(input()) for _ in range(N)]
sorta = sorted(set(a))

for i in a:
    print(bisect.bisect_left(sorta, i))
