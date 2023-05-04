T = int(input())

for i in range(T):
    N = int(input())
    if N % 2 == 0 and N % 4 != 0:
        print('Same')
    elif N % 2 == 1:
        print('Odd')
    else:
        print('Even')
