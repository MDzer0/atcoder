N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
atotal = 1
btotal = 1
for i in a:
    atotal *= i

for i in b:
    btotal *= i

if atotal == btotal:
    print('Yes')
else:
    print('No')
