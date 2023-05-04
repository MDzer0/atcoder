N = int(input())
A = 0
B = 0
for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        A += a + b
    elif b > a:
        B += a + b
    else:
        A += a
        B += b
print(A, B)
