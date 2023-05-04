N = int(input())
S = input()
left = S[:N//2]
right = S[N//2:]
cnt = 0
if N % 2 != 0:
    print(-1)
    exit()

for i in range(N // 2):
    if left[i] != right[i]:
        cnt += 1

print(cnt)
