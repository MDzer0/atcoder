T = int(input())
X = [int(input()) for _ in range(T)]

for i in range(T):
    ansB = X[i]
    a, b = 1, 1

    while X[i] > a:
        if (X[i] - a) % b == 0:
            ansB = min(ansB, (X[i] - a) // b)
        a, b = b, a + b
    print(1, ansB)
