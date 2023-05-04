N = int(input())
S = input()
T = ''
for i in S:
    T = T.replace(i, '')
    T += i
print(T)
