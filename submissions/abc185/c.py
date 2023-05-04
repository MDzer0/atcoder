L = int(input())
ans = 1
for i in range(L - 1, L - 12, -1):
    ans *= i

waru = 1
for i in range(1, 12):
    waru *= i

print(ans // waru)
