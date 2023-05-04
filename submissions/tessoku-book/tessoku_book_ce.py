N = int(input())
A = list(map(int, input().split()))
atari = [0] * (N + 1)
hazure = [0] * (N + 1)

for i in range(N):
    if A[i] == 1:
        atari[i + 1] = atari[i] + 1
        hazure[i + 1] = hazure[i]
    else:
        atari[i + 1] = atari[i]
        hazure[i + 1] = hazure[i] + 1

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    atariCnt = atari[r] - atari[l - 1]
    hazureCnt = hazure[r] - hazure[l - 1]
    if atariCnt > hazureCnt:
        print('win')
    elif hazureCnt > atariCnt:
        print('lose')
    else:
        print('draw')
