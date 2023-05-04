BTCIN = 'BTC'
BTCTAN = 380000.0
inNinzu = int(input())
okaneList = [[0 for i in range(2)] for j in range(inNinzu)]
okaneAns = 0.0
for i in range(0, inNinzu):
    inOkane = input().split(' ')
    if inOkane[1] == BTCIN:
        okaneAns += float(inOkane[0]) * BTCTAN
    else:
        okaneAns += float(inOkane[0])

print(okaneAns)
