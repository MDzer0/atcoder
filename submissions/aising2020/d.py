n = int(input())
s = input()
x = [0] * n

def pcnt(x):
    return bin(x).count('1')

def f(x):
    if x == 0: return 0
    return f(x % pcnt(x)) + 1

for i in range(n):
    x[i] = int(s[i])

pc = sum(x)
ans = [0] * n
for b in range(2):
    npc = pc
    if b == 0:
        npc += 1
    else:
        npc -= 1

    if npc <= 0: continue

    r0 = 0
    for i in range(n):
        r0 = (r0 * 2) % npc
        r0 += x[i]

    k = 1
    for i in range(n - 1, -1, -1):
        if x[i] == b:
            r = r0
            if b == 0:
                r = (r + k) % npc
            else:
                r = (r - k + npc) % npc
            ans[i] = f(r) + 1
        k = (k * 2) % npc

for i in ans:
    print(i)
