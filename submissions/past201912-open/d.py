N = int(input())
a = [int(input()) for _ in range(N)]
c = [0] * N

for i in range(N):
    c[a[i] - 1] += 1

w, r = 0, 0
for i in range(N):
    if c[i] == 0:
        r = i + 1
    elif c[i] == 2:
        w = i + 1

if r == 0 and w == 0:
    print('Correct')
else:
    print(w, r)
