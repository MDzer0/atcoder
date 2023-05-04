N = int(input())
ansMax = 0
for i in range(10**5):
    tmp = i ** 2
    if tmp <= N:
        ansMax = tmp
    #else:
    #    break

print(ansMax)
