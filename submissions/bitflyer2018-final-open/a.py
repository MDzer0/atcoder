N = int(input())
ans = 10 ** 10
for i in range(N):
    p = input()
    tmp = 0
    for i in range(len(p)):
        if p[-i - 1] == '0':
            tmp += 1
        else:
            ans = min(ans, tmp)
            break
print(ans)
