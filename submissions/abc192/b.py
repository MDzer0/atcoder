S = input()

for i in range(len(S)):
    if i % 2 == 0:
        if S[i].islower():
            continue
        else:
            print('No')
            exit()
    else:
        if S[i].isupper():
            continue
        else:
            print('No')
            exit()
print('Yes')
