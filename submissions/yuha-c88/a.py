import sys
read = sys.stdin.read

n,*pqr = read().split()

ans = ''
it = iter(pqr)
for p,q,r in zip(it,it,it):
    if p == 'BEGINNING':
        ans += r[0]
    elif p == 'END':
        ans += r[-1]
    else:
        l = len(r)
        ans += r[l//2]
print(ans)
