a, b, c = map(int, input().split())
if c == 1:
    print('No')
    exit()
    
tmp = 1
for i in range(1, b + 1):
    tmp *= c
    if a < tmp:
        print('Yes')
        exit()

print('No')
