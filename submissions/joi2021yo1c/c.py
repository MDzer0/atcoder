N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in A:
    for j in B:
        if i <= j:
            cnt += 1

print(cnt)
