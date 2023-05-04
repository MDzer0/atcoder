N = int(input())
Slist = list(map(str, input().split()))

yCnt = Slist.count('Y')

if yCnt >= 1:
    print('Four')
else:
    print('Three')
