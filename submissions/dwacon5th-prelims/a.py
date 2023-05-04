N = int(input())
a = list(map(int, input().split()))
av = sum(a) / N
tmp = 101
index = 0
for i in range(N):
    if tmp > abs(a[i] - av):
        tmp = abs(a[i] - av)
        index = i

print(index)
