N = int(input())
if N <= 52:
    print(N//2*3 + N%2)
    exit()
w = 1
ans = 0
while N >= 26**w:
    N -= 26**w
    ans += w * 26**w
    w += 1
ans += w * N
print(ans)
