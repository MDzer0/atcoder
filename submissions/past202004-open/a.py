S, T = input().split()

if S[0] == 'B':
    S = -int(S[1]) + 1
else:
    S = int(S[0])

if T[1] == 'F':
    T = int(T[0])
else:
    T = -int(T[1]) + 1

print(abs(S - T))
