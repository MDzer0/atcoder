s = input()
ans = ''
for i in range(len(s)):
    if s[i] == '0':
        ans += '0'
    elif s[i] == '1':
        ans += '1'
    else:
        ans = ans[0:-1]
print(ans)
