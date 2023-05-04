def GCD(a, b):
    while a >= 1 and b >= 1:
        if a < b:
            b = b % a
        else:
            a = a % b
    if a >= 1:
        return a
    else:
        return b

def LMC(a, b):
    return (a * b) // GCD(a, b)

N = int(input())
A = list(map(int, input().split()))

ans = LMC(A[0], A[1])
for i in range(2, N):
    ans = LMC(ans, A[i])

print(ans)
