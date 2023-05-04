N = int(input())
S = [""] * N
for i in range(N):
    S[i] = input()
T = input()

start = 1
end = N+2
for s in S:
    s_a = s.replace("?", "a")
    s_z = s.replace("?", "z")
    if s_z < T:
        start += 1
    if T < s_a:
        end -= 1

ans = list(range(start, end))
print(*ans)
