def solve(a, b):
    total = 0
    for i in range(N):
        omote = AB[i][0]
        ura = AB[i][1]
        if a == 2:
            omote = -AB[i][0]
        if b == 2:
            ura = -AB[i][1]
        if omote + ura >= 0:
            total += omote + ura
    return total

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
pattern1 = solve(1, 1)
pattern2 = solve(2, 1)
pattern3 = solve(1, 2)
pattern4 = solve(2, 2)

print(max(pattern1, pattern2, pattern3, pattern4))
