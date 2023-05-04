X = int(input())
ansMax = 0
for i in range(1, X + 1):
    for j in range(2, X + 2):
        tmp = i ** j
        if X >= tmp:
            ansMax = max(ansMax, tmp)
        else:
            break

print(ansMax)
