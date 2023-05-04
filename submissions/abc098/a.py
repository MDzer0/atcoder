A, B = map(int, input().split())

minAns = -1000001
tmp1 = A + B
tmp2 = A * B
tmp3 = A - B
minAns = max(minAns, tmp1, tmp2, tmp3)

print(minAns)
