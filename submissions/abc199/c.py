N = int(input())
S = list(input())
Q = int(input())

hanten = 0
for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if hanten % 2 == 1:
            if a < N:
                a = a + N
            else:
                a = a - N
            if b < N:
                b = b + N
            else:
                b = b - N
        tmp = S[a - 1]
        S[a - 1] = S[b - 1]
        S[b - 1] = tmp
    else:
        hanten += 1

if hanten % 2 == 1:
    print(''.join(S[N:2 * N]) + ''.join(S[:N]))
else:
    print(''.join(S))
