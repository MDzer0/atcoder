ca = input().split()
cb = input().split()

if ca[0] == cb[0]:
    print(abs(int(ca[1]) - int(cb[1])) // 15)
else:
    print(abs(int(ca[1]) + int(cb[1])) // 15)
