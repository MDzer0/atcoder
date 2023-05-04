import bisect

INDEX = 10 ** 6 + 1
sosu = [1] * INDEX

def eratosh():
    sosu[0] = 0
    sosu[1] = 0
    for i in range(2, INDEX):
        if sosu[i] == 0:
            continue
        for j in range(2 * i, INDEX, i):
            sosu[j] = 0
    return

N = int(input())
eratosh()
sosuList = []
for i in range(INDEX):
    if sosu[i]:
        sosuList.append(i)

ans = 0
for i in range(1, len(sosuList)):
    tmp = sosuList[i] ** 3
    if tmp * 2 <= N:
        left = 0
        right = bisect.bisect_right(sosuList, sosuList[i])
        while right - left > 1:
            mid = (left + right) // 2
            if tmp * sosuList[mid] <= N:
                left = mid
            else:
                right = mid
        ans += min(i, right)
print(ans)
