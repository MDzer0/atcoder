N = int(input())
f, a = 0, 0
for i in range(N):
    if input() == "For":
        f += 1
    else:
        a += 1

if f > a:
    print("Yes")
else:
    print("No")
