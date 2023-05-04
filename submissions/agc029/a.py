S = input()
B = S.count('B')
W = S.count('W')
es = 'W' * W + 'B'* B
bf = es.find('B')
blst = [0] * B
for i in range(B):
    blst[i] = bf + i
slst = [0] * B
bindex = 0
for i in range(len(S)):
    if S[i] == 'B':
        slst[bindex] = i
        bindex += 1

ans = 0
for i in range(B):
    ans += blst[i] - slst[i]

print(ans)
