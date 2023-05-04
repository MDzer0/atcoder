A, B = map(str, input().split())
ans = -10 ** 5
for i in range(3):
    ans = max(ans, int(A[0:i] + '9' + A[i + 1:]) - int(B))
    if i == 0:
        ans = max(ans, int(A) - int('1' + B[1:]))
    else:
        ans = max(ans, int(A) - int(B[0:i] + '0' + B[i + 1:]))

print(ans)
