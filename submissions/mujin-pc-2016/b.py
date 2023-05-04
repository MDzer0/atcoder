import math
a, b, c = map(int, input().split())
hankei = a + b + c
maxabc = max(a, b, c)
kuran = 0
if maxabc - (a + b + c - maxabc) > 0:
    kuran = maxabc - (a + b + c - maxabc)
print((hankei ** 2 * math.pi) - (kuran ** 2 * math.pi))
