A, B = map(int, input().split())

def F(v):
    tmp = v // 2
    amari = v % 2
    ans = 0
    if tmp % 2 == 0:
        if amari != 0:
            ans = v - 1
    else:
        if amari != 0:
            ans = 1 ^ (v - 1)
        else:
            ans = 1
    return ans

ansA = F(A)
ansB = F(B + 1)
print(ansA ^ ansB)
