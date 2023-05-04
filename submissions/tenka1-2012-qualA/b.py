c = input()
ans = c.split()
tmp = ''
for i in ans:
    tmp += i + ','

print(tmp[:-1])
