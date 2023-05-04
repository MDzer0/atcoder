S = input()
findlst1 = ['I', 'C', 'T']
findlst2 = ['i', 'c', 't']
index = 2
for i in range(len(S) - 1, -1, -1):
    if S[i] == findlst1[index] or S[i] == findlst2[index]:
        index -= 1
    if index == -1:
        break

if index == -1:
    print('YES')
else:
    print('NO')
