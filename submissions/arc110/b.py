N = int(input())
S = input()

if S == '1':
    print(10 ** 10 * 2)
elif S == '11':
    print(10 ** 10)
else:
    if S.count('111') + S.count('010') + S.count('00') > 0:
        print(0)
        exit()
    cnt = S.count('0')
    if S[-1] == '0':
        print(10 ** 10 - cnt + 1)
    else:
        print(10 ** 10 - cnt)
