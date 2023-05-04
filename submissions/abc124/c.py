S = input()
slist = []
for i in S:
    slist.append(i)

ans = 0

for i in range(1, len(S)):
    if slist[i - 1] == slist[i]:
        if slist[i] == '0':
            slist[i] = '1'
            ans += 1
        else:
            slist[i] = '0'
            ans += 1
print(ans)
