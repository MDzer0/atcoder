import string
abc = string.ascii_lowercase
s = list(input())
K = int(input())
index = 0
while K > 0:
    if index == len(s) - 1:
        s[index] = abc[(abc.index(s[index]) + K) % 26]
        break
    tmp = 26 - abc.index(s[index])
    if tmp == 26:
        index += 1
        continue
    if K >= tmp:
        s[index] = 'a'
        index += 1
        K -= tmp
    else:
        index += 1

for i in s:
    print(i, end='')
