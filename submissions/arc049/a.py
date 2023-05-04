S = list(input())
a = list(map(int, input().split()))

for i in range(4):
    S.insert(a[i] + i, '"')

for i in range(len(S)):
    if i != len(S) - 1:
        print(S[i], end='')
    else:
        print(S[i])
