N = int(input())
a, b = divmod(N, 9)
if b == 0:
    b = 9
    a -= 1
print(str(b) * (a + 1))
