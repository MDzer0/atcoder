N, K = map(int, input().split())
da = []
nlist = [0] * N
for i in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        nlist[j - 1] += 1

print(nlist.count(0))
