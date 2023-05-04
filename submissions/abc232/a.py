S = input()
index = S.index('x')
print(int(S[:index]) * int(S[index + 1:]))
