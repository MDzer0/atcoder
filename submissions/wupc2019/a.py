s = input()
ans = ''
for i in range(len(s) - 2, -1, -1):
    if s[i: i + 2] == 'WA':
        s = s[0: i] + 'AC' + s[i + 2:]

print(s)
