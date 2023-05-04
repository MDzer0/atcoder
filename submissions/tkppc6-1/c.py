N = int(input())
A = list(map(int, input().split()))
mound = A[0]
tyuo = (2 * N - 1) // 2
for i in range(len(A)):
    if A[i] == -1:
        A[i] = mound

A.sort()
mound_cnt = A.count(mound)
index = A.index(mound)
if index <= tyuo <= index + mound_cnt:
    print('Yes')
else:
    print('No')
