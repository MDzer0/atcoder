H, A = map(int, input().split())

cnt = 0
for i in range(H):
    if H <= 0:
        break
    else:
        cnt += 1
        H -= A

print(cnt)
