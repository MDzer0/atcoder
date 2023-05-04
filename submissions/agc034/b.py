s = input()
s = s.replace('BC', 'D')
ans = []
tmp = 0
for i in reversed(range(len(s))):
    if s[i] == 'D':
        tmp += 1
    elif s[i] == 'A':
        ans.append(tmp)
    else:
        tmp = 0

print(sum(ans))
