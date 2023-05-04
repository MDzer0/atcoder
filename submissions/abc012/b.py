N = int(input())

hh = str(N // 3600).zfill(2)
tmp = N % 3600
mm = str(tmp // 60).zfill(2)
tmp = tmp % 60
ss = str(tmp).zfill(2)
print(hh + ':' + mm + ':' + ss)
