N = int(input())
ans = 0
for i in range(1, 10):
    if N == int(str(i) + str(i) + str(i)):
        ans = int(str(i) + str(i) + str(i))
        break
    elif N < int(str(i) + str(i) + str(i)):
        ans = int(str(i) + str(i) + str(i))
        break

print(ans)
