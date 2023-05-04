import bisect
N = int(input())
A = list(map(int, input().split()))
setA = set(A)
sortA = sorted(list(setA))

B = []
for i in A:
    B.append(bisect.bisect_left(sortA, i) + 1)

print(*B)
