def segfunc(x, y): return max(x, y)

def init(tmpn):
    global noden
    n = 1
    while tmpn > n:
        n *= 2
    noden = n

def update(i, x):
    i += noden-1
    node[i] = x
    while i:
        i = (i-1)//2
        node[i] = segfunc(node[i*2+1], node[i*2+2])

def query(l, r):
    L = l + noden
    R = r + noden
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = segfunc(s, node[R - 1])
        if L & 1:
            s = segfunc(s, node[L - 1])
            L += 1
        L >>= 1
        R >>= 1
    return s

N, Q = map(int, input().split())
MAX_N = 2**(N-1).bit_length()
node = [0] * (2 * MAX_N - 1)
noden = 0
INF = 0

init(N)
lsta = list(map(int, input().split()))
for i in range(N):
    update(i, lsta[i])

for i in range(Q):
    x, y, z = map(int, input().split())
    if x == 1:
        update(y - 1, z)
    elif x == 2:
        print(query(y - 1, z))
    else:
        under = y - 1
        top = N + 1
        while top - under > 1:
            mid = (under + top) // 2
            if query(under, mid) >= z:
                top = mid
            else:
                under = mid
        print(top)
