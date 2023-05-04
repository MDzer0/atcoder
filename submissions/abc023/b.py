import sys

N = int(input())
S = input()

if N % 2 == 0:
    print(-1)
    sys.exit()

ans = (N - 1) // 2
acc = "b"

for i in range(ans):
    if i % 3 == 0:
        acc = "a" + acc + "c"
    elif i % 3 == 1:
        acc = "c" + acc + "a"
    else:
        acc = "b" + acc + "b"

if S == acc:
    print(ans)
else:
    print(-1)
