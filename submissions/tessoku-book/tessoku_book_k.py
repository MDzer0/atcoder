N, X = map(int, input().split())
A = list(map(int, input().split()))

low = 0
up = N
while up - low > 1:
    mid = (up + low) // 2
    if A[mid] == X:
        print(mid + 1)
        exit()
    if A[mid] < X:
        low = mid
    else:
        up = mid
