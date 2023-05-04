N = int(input())
takolist = []

for i in range(N):
    takolist.append(int(input()))

takolist = sorted(takolist)
print(takolist[0])
