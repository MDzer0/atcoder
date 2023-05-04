X, Y = map(str, input().split())

if X > Y:
    print('>')
elif Y > X:
    print('<')
else:
    print('=')
