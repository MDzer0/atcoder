N = int(input())
A, B = map(int, input().split())
p = list(map(int, input().split()))
oneCnt = 0
twoCnt = 0
treeCnt = 0
for i in p:
    if i <= A:
        oneCnt += 1
    elif A + 1 <= i <= B:
        twoCnt += 1
    else:
        treeCnt += 1

print(min(oneCnt, twoCnt, treeCnt))
