A, B, C = map(int, input().split())

if C == 1:
    if B == 0:
        print('Takahashi')
        exit()
    B -= 1
else:
    if A == 0:
        print('Aoki')
        exit()

for i in range(201):
    if i % 2 == 0:
        A -= 1
        if A == 0:
            print('Aoki')
            exit()
    else:
        B -= 1
        if B == 0:
            print('Takahashi')
            exit()
