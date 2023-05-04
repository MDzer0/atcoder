import string
S = input()
ans = ''
for i in S:
    if string.ascii_lowercase.count(i) == 0\
             and string.ascii_uppercase.count(i) == 0:
        ans += i

print(ans)
