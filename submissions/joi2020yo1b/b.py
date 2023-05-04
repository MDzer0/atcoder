N, A, B = map(int, input().split())
S = input()
if A != B:
    ans = S[:A - 1] + S[A - 1:B][::-1] + S[B:]
else:
    ans = S
print(ans)
