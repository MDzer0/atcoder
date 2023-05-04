X, A, B = map(int, input().split())

tmp = A - B

if tmp >= 0:
    print('delicious')
elif X >= abs(tmp):
    print('safe')
else:
    print('dangerous')
