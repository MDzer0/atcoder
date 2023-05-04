X = input()
count = X.count(X[0])

if count == 4:
    print('Weak')
else:
    tmp = int(X[0])
    cnt = 0
    for i in X[1:]:
        if int(i) == (tmp + 1) % 10:
            cnt += 1
        tmp = int(i)

    if cnt == 3:
        print('Weak')
    else:
        print('Strong')
