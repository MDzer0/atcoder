Y, M, D = map(int, input().split())
ans = 'NOT CHRISTMAS DAY'
if M == 12 and D == 25:
    print(Y - 2018)
else:
    print(ans)
