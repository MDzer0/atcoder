import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()

for i in range(Q):
    b = int(input())
    index = bisect.bisect_left(A, b)
    if index != 0 and index != N:
        print(min(abs(A[index - 1] - b), abs(A[index] - b)))
    elif index == 0:
        print(abs(A[index] - b))
    else:
        print(abs(A[index - 1] - b))
