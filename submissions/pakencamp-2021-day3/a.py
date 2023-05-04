ans = 0
for i in range(4):
    s = input()
    if s.count('1') == 4:
        ans += 1

print(ans)
