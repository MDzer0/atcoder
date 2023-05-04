X = input()
ans = 0
for i in X:
    ans = max(int(i), ans)
print(ans)
