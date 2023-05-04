from collections import defaultdict

S = input()
d = defaultdict(int)
for i in S:
    d[i] += 1

if len(d) == 1 or len(d) == 3:
    print('No')
else:
    if len(d) == 4:
        print('Yes')
    elif 'N' in d:
        if 'S' in d:
            print('Yes')
        else:
            print('No')
    elif 'W' in d:
        if 'E' in d:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
