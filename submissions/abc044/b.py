import sys

w = input()

if len(w) % 2 == 1:
    print('No')
    sys.exit()

for i in range(len(w)):
    if w.count(w[i]) % 2 == 1:
        print('No')
        sys.exit()

print('Yes')
