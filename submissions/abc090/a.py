ans = ''
for i in range(3):
    for j in range(3):
        if i == j:
            tmp = input()
            ans += tmp[i]

print(ans)
