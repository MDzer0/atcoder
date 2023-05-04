H = int(input())
W = int(input())
N = int(input())
a, m = divmod(N, max(H, W))
if m != 0:
    a += 1
print(a)
