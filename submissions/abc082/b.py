s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)
ss = ''.join(s)
ts = ''.join(t)

if s < t:
    print('Yes')
else:
    print('No')
