N = int(input())
ans, mod = divmod(N, 400)
if mod != 0:
    print(ans + 1)
else:
    print(ans)
