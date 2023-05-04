import sys
e = list(map(int, input().split()))
B = int(input())
l = list(map(int, input().split()))
r = -1
cnt = 0
for i in range(6):
    if e.count(l[i]) == 1:
        cnt += 1
    else:
        r = l[i]

if cnt == 5:
    if r == B:
        print(2)
        sys.exit()
if cnt == 6:
    print(1)
elif cnt == 5:
    print(3)
elif cnt == 4:
    print(4)
elif cnt == 3:
    print(5)
else:
    print(0)
