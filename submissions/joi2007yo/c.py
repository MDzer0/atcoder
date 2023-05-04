import string
ans = ''
S = input()
for i in S:
    ind = list(string.ascii_uppercase).index(i)
    ans += string.ascii_uppercase[ind - 3]

print(ans)
