A, B = map(int, input().split())
ans = A * B
ans -= A + B - 1
print(ans)
