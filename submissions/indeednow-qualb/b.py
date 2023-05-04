s = input()
t = input()

if s == t:
    print(0)
    quit()

for i in range(1, len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        print(i)
        quit()

print(-1)
