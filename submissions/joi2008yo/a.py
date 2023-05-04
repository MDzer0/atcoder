okane = 1000
oturi = 1000 - int(input())
cnt = 0
kouka = [500, 100, 50, 10, 5, 1]
for i in kouka:
    cnt += oturi // i
    oturi %= i

print(cnt)
