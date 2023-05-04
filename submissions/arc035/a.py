s = input()
slen = len(s) // 2
ans = 'YES'
for i in range(slen):
    if s[i] == s[-i - 1] or s[-i - 1] == '*' or s[i] == '*':
        continue
    else:
        ans = 'NO'
        break

print(ans)
