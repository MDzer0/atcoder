N = int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(N):
    if i + 1 == A[i]:
        continue
    else:
        print('No')
        exit()
print('Yes')
