import fractions

A, B, C, D = map(int, input().split())
A -= 1
tmp = fractions.gcd(C, D)
lcd = (C * D) // tmp
acnt1 = A // C
acnt2 = A // D
acnt3 = B // C
acnt4 = B // D
acnt5 = A // lcd
acnt6 = B // lcd
ans = B - A
atmp = acnt3 + acnt4 - acnt1 - acnt2 + acnt5 - acnt6
ans -= atmp
print(ans)
