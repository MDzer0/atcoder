import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())

for i in range(Q):
    X = int(input())
    print(bisect.bisect_left(A, X))
