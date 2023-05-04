A = int(input())
B = int(input())
alist = [1, 2, 3]

for i in alist:
    if A == i or B == i:
        continue
    else:
        print(i)
