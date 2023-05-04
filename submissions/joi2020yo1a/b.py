N = int(input())
S = input()
cnt = 0
clist = ['a', 'i', 'u', 'e', 'o']
for i in clist:
    cnt += S.count(i)

print(cnt)
