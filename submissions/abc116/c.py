import sys

N = int(input())
h = list(map(int, input().split()))
cnt = 0
start = 0
end = 0
if sum(h) == 0:
    print(0)
    sys.exit()

while True:
    for i in range(N):
        if h[i] != 0:
            start = i
            break

    end = N
    for i in range(start + 1, N):
        if h[i] == 0:
            end = i
            break

    for i in range(start, end):
        if h[i] != 0:
            h[i] = h[i] - 1

    cnt += 1
    start = 0
    end = 0
    if sum(h) == 0:
        break

print(cnt)
