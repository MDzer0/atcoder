S = input()
a, b = map(int, input().split())
print(S[:a - 1] + S[b - 1: b] + S[a: b - 1] + S[a - 1:a] + S[b:])
