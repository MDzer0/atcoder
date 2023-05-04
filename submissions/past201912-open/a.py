import string
S = input()
for i in S:
    if string.ascii_lowercase.count((i)) != 0:
        print('error')
        exit()

print(int(S) * 2)
