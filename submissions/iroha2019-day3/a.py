# Iroha2019-3A - ‰F’ˆl
def main():
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = map(
        int, input().split()
    )
    print(A - B)  # Q.1
    print(C + D)  # Q.2
    print(0 if E > F else F - E + 1)  # Q.3
    print(((G + H + I) // 3 + 1))  # Q.4
    print(
        ["", "a", "aa", "aaa", "aaai", "aaaji", "aabaji", "agabaji", "dagabaji"][J]
    )  # Q.5
    # Q.6-7
    fav1 = K
    for i in range(61):
        if fav1 % 61 == L:
            break
        fav1 += 59
    fav1 += 59 * 61 * (M - 1)
    perfect = [8589869056, 33550336, 8128, 496, 28, 6]
    fav2 = perfect[0]
    for n in perfect:
        if abs(fav1 - n) >= N:
            fav2 = n
    print(min(fav1, fav2), max(fav1, fav2), sep="\n")
    print(((O + P + Q) * (R + S + T) * (U + V + W) * (X + Y + Z)) % 9973)


if __name__ == "__main__":
    main()
