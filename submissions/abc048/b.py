a, b, c = map(int, input().split())

ans = b // c
ans -= (a - 1) // c
print(ans)
