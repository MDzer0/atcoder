def update(pos, x):
    pos = pos + size
    rmq[pos] = x
    while pos >= 2:
        pos //= 2
        rmq[pos] = max(rmq[pos * 2], rmq[pos * 2 + 1])

def query(l, r, a, b, u):
    if r <= a or b <= l:
        return -10 ** 18
    if l <= a and b <= r:
        return rmq[u]
    m = (a + b) // 2
    ansl = query(l, r, a, m, 2 * u)
    ansr = query(l, r, m, b, 2 * u + 1)
    return max(ansl, ansr)

N, Q = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(Q)]

size = 1
while size < N:
    size *= 2
rmq = [0] * (2 * size)

for tmp in q:
    if tmp[0] == 1:
        update(tmp[1] - 1, tmp[2])
    else:
        ans = query(tmp[1] - 1, tmp[2] - 1, 0, size, 1)
        print(ans)
