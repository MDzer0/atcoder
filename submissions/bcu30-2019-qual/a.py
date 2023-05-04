N, P = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if P >= i:
        cnt += 1
        P -= i
    else:
        break
print(cnt)
