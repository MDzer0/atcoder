s = input()

indexa = 0
indexz = 0
for i in range(len(s)):
    if s[i] == 'A':
        indexa = i
        break

for i in range(len(s) - 1, 0, -1):
    if s[i] == 'Z':
        indexz = i
        break

print(indexz - indexa + 1)
