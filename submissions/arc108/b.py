N = int(input())
s = input()
tmp = ''
cnt = 0
for i in s:
    tmp += i
    cnt += 1
    if cnt >= 3:
        if tmp[len(tmp) - 3:] == 'fox':
            tmp = tmp[:len(tmp) - 3]
print(len(tmp))
