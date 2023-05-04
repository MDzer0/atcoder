N = int(input())
s = input()
t = input()

ans = len(s) + len(t)
index = 0
tmp = 0
for i in range(len(s)):
    if s[-i - 1] == t[index]:
        index += 1
        for j in range(len(s) - i, len(s)):
            if s[j] == t[index]:
                index += 1
            else:
                break
        tmp = max(tmp, index)
        index = 0


print(ans - tmp)
