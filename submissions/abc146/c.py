A, B, C = map(int, input().split())
ans = 0
index = '1'
while True:
    tmp = (A * int(index)) + (B * len(index))

    if tmp >= C:
        break

    ans = max(ans, int(index))
    index += '0'
    if tmp == 0:
        break
if tmp == C:
    ans = index
    print(ans)
else:
    ans = 0
    index = str(int(index) - 1)
    for i in range(len(index)):
        for j in range(10):
            index = index[:i] + str(j) + index[i + 1:]
            tmp = (A * int(index)) + (B * len(index))
            if tmp > C:
                break
            ans = max(ans, int(index))

if ans >= 10 ** 9:
    ans = 10 ** 9
print(ans)
