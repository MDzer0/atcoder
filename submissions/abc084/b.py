A, B = map(str, input().split())
S = input()

if S[0:int(A)].isdigit() and S[int(A)] == '-' and S[int(A) + 1:].isdigit():
    print('Yes')
else:
    print('No')
