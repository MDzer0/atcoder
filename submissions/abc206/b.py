N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += i
    if N <= ans:
        print(i)
        exit()