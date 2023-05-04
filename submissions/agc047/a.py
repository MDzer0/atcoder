from collections import defaultdict

def calc(a):
    a1, a2 = 0, 0
    if '.' in a:
        a = a.rstrip('0')
        cnt = len(a) - a.index('.') - 1
        a1, a2 = -cnt, -cnt
    a = int(a.replace('.', ''))

    while a % 2 == 0:
        a1 += 1
        a //= 2
    while a % 5 == 0:
        a2 += 1
        a //= 5
    return a1, a2

d = defaultdict(int)
N = int(input())
A = []
for _ in range(N):
    a = input()
    a1, a2 = calc(a)
    d[(a1, a2)] += 1

ans = 0
key = list(d.keys())
for i in range(len(key)):
    a1, a2 = key[i]
    v = d[(a1, a2)]
    if a1 >= 0 and a2 >= 0:
        ans += v * (v - 1) // 2
    for j in range(i + 1, len(key)):
        b1, b2 = key[j]
        if (a1 + b1) >= 0 and (a2 + b2) >= 0:
            ans += v * d[(b1, b2)]

print(ans)
