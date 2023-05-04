N = int(input())
ctr = 0
while N > 0:
    if ctr % 2 == 0:
        N //= 2
    else:
        N = (N - 1) // 2
    ctr += 1
if ctr % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")
