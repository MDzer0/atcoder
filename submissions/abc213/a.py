A, B = map(int, input().split())
for i in range(256):
    tmp = A ^ i
    if B == tmp:
        print(i)
        exit()
