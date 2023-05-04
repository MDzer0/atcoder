N, K = map(int, input().split())
S = input()
if 1 == K:
    print(S[K - 1].lower() + S[K::])
else:
    print(S[:K - 1] + S[K - 1].lower() + S[K::])
