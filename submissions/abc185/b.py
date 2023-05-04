N, M, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
a = N

jikoku = 0
for i in range(M):
    A, B = AB[i][0], AB[i][1]
    sa = A - jikoku
    a -= sa
    if a < 1:
        print('No')
        exit()
    a = min(B - A + a, N)
    jikoku = B

sa = T - jikoku
a -= sa
if a < 1:
    print('No')
else:
    print('Yes')
