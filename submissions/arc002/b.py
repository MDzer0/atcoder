import datetime

year = input()
Y, M, D = map(int, year.split('/'))
now = datetime.datetime(Y, M, D)
tmp = now.year % (now.month * now.day)

while True:

    if tmp == 0:
        print(now.strftime('%Y/%m/%d'))
        break

    now += datetime.timedelta(days=1)
    tmp = now.year % (now.month * now.day)
