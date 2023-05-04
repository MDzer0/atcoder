S = input()
L, R = map(int, input().split())

if S[0] == '0' and len(S) > 1:
    print('No')
    exit()

if L <= int(S) <= R:
    print('Yes')
else:
    print('No')
