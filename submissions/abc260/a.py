s = list(input())

for i in range(3):
    if s.count(s[i]) == 1:
        print(s[i])
        break
else:
    print(-1)
