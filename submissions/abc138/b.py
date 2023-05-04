from fractions import Fraction
N = int(input())
aLst = list(map(int, input().split()))
ansLst = []
for i in range(N):
    ansLst.append(Fraction(1, aLst[i]))

print(float(Fraction(1, sum(ansLst))))
